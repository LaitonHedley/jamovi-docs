#!/usr/bin/env python3
"""Post-process pandoc-converted MDX files to fix Sphinx/RST-specific patterns."""
import re
from pathlib import Path

DOCS_DIR = Path("src/content/docs")

LOCALE_DIRS = {
    'ar', 'da', 'de', 'es', 'fi', 'fr', 'hr', 'is', 'it', 'ja', 'ko',
    'nb', 'nn', 'pl', 'pt', 'ru', 'si', 'sl', 'sv', 'ta', 'tr', 'uk',
    'vi', 'zh_CN', 'zh_TW',
}


def fix_image_path(path: str) -> str:
    path = re.sub(r'^\.\./_images/', '/images/', path)
    path = re.sub(r'^/_images/', '/images/', path)
    path = re.sub(r'^_images/', '/images/', path)
    return path


def convert_image_attrs(m: re.Match) -> str:
    """Convert pandoc image syntax ![alt](path){attrs} to MDX-safe HTML."""
    alt = m.group(1)
    path = fix_image_path(m.group(2))
    attrs_raw = m.group(3) or ''

    style_parts = []
    width = re.search(r'width="([^"]+)"', attrs_raw)
    height = re.search(r'height="([^"]+)"', attrs_raw)
    if width:
        w = width.group(1)
        if re.match(r'^\d+$', w):
            w += 'px'
        style_parts.append(f'width: {w}')
    if height:
        h = height.group(1)
        if re.match(r'^\d+$', h):
            h += 'px'
        style_parts.append(f'height: {h}')

    style = '; '.join(style_parts)
    alt_escaped = alt.replace('"', '&quot;')

    if style:
        return f'<img src="{path}" alt="{alt_escaped}" style="{style}" />'
    # No size attrs — plain markdown image is fine
    return f'![{alt}]({path})'


def process_file(path: Path) -> None:
    text = path.read_text(encoding='utf-8')

    # 1. Remove sectionauthor fenced divs produced by pandoc
    #    Pattern: ::: sectionauthor\ncontent\n:::
    text = re.sub(
        r':::\s*sectionauthor\n.*?\n:::\n?',
        '', text, flags=re.DOTALL
    )

    # 2. Convert pandoc note/warning/tip fenced divs to Starlight asides.
    #    Pandoc outputs 4-colon outer divs:
    #      :::: note
    #      ::: title
    #      Note
    #      :::
    #
    #      content
    #      ::::
    ASIDE_MAP = {
        'note': 'note', 'warning': 'caution', 'caution': 'caution',
        'tip': 'tip', 'important': 'danger', 'hint': 'tip',
        'danger': 'danger', 'error': 'danger',
    }
    aside_pattern = r'::::\s*(' + '|'.join(ASIDE_MAP.keys()) + r')\n(.*?)::::'

    def replace_aside(m: re.Match) -> str:
        kind = ASIDE_MAP.get(m.group(1).lower(), 'note')
        inner = m.group(2)
        # Remove the inner ::: title\nXxx\n::: block
        inner = re.sub(r':::\s*title\n.*?\n:::\n?', '', inner, flags=re.DOTALL)
        inner = inner.strip()
        return f':::{kind}\n{inner}\n:::'

    text = re.sub(aside_pattern, replace_aside, text, flags=re.DOTALL | re.IGNORECASE)

    # 3. Convert images with pandoc attribute syntax  ![alt](path){...}
    #    Must handle inline images too (e.g. icon with height attr)
    text = re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)(\{[^}]*\})?',
        convert_image_attrs, text
    )

    # 4. Fix any remaining bare _images/ paths not caught above
    text = re.sub(r'src="/_images/', 'src="/images/', text)
    text = re.sub(r'src="../_images/', 'src="/images/', text)

    # 5. Convert :doc: cross-refs left by pandoc as interpreted-text spans
    #    Form: `slug`{.interpreted-text role="doc"}
    def doc_ref(m: re.Match) -> str:
        slug = m.group(1).strip()
        label = Path(slug).name
        return f'[{label}](../{slug}.mdx)'

    text = re.sub(
        r'`([^`]+)`\{\.interpreted-text\s+role="doc"\}',
        doc_ref, text
    )

    # 6. Strip :ref: spans — keep just the label text
    text = re.sub(r'`([^`]+)`\{\.interpreted-text\s+role="ref"\}', r'\1', text)

    # 7. Add MDX frontmatter if missing
    if not text.startswith('---'):
        heading = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
        title = heading.group(1).strip() if heading else path.stem
        # Escape double quotes in title
        title = title.replace('"', '\\"')
        text = f'---\ntitle: "{title}"\n---\n\n' + text

    # 8. Collapse runs of 3+ blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    path.write_text(text.strip() + '\n', encoding='utf-8')
    print(f'  {path}')


def main() -> None:
    mdx_files = [
        f for f in DOCS_DIR.glob('**/*.mdx')
        if not any(part in LOCALE_DIRS for part in f.parts)
    ]
    print(f'Processing {len(mdx_files)} English MDX files...')
    for f in sorted(mdx_files):
        process_file(f)
    print(f'\nDone.')


if __name__ == '__main__':
    main()
