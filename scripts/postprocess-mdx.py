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

    # 1a. Strip blockquote markers — RST body text is indented (= RST block quote),
    #     pandoc converts that to "> " prefixes, but all content here is plain prose.
    # Handles both top-level ("> text") and indented ("  > text") blockquotes.
    # Bare ">" lines are paragraph separators — convert to blank lines first.
    text = re.sub(r'^(\s*)>\s*$', r'\1', text, flags=re.MULTILINE)
    text = re.sub(r'^(\s*)> ', r'\1', text, flags=re.MULTILINE)

    # 1b. Normalize code fence language tags: lowercase and strip extra spaces
    #     pandoc emits "``` R" (space before lang); standardise to "```r"
    def _norm_fence(m: re.Match) -> str:
        lang = m.group(2).lower()
        if lang == 'rout':
            lang = 'r'
        return m.group(1) + lang
    text = re.sub(r'^(\s*```+)\s+([A-Za-z][A-Za-z0-9]*)\s*$', _norm_fence, text, flags=re.MULTILINE)

    # 1. Remove sectionauthor fenced divs produced by pandoc
    #    Pattern: ::: sectionauthor\ncontent\n:::
    text = re.sub(
        r':::\s*sectionauthor\n.*?\n:::\n?',
        '', text, flags=re.DOTALL
    )

    # 2a. Remove pandoc fenced divs for toctree/contents directives.
    #     These appear as :::: {.toctree ...}\n...\n:::: or inside blockquotes.
    text = re.sub(r'^(?:>{1,2}\s+)?:{3,4}\s*\{\.(?:toctree|contents)[^}]*\}.*?:{3,4}', '', text, flags=re.DOTALL | re.MULTILINE)
    # Clean up any empty blockquote lines left behind
    text = re.sub(r'(^>\s*\n)+', '', text, flags=re.MULTILINE)

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

    # 4b. Convert <div class="gif-player"> markup to <video> elements.
    #     GIFs have been converted to WebM + MP4 via scripts/convert-gifs.sh.
    def gif_player_to_video(m: re.Match) -> str:
        attrs = m.group(1)
        anim = re.search(r'data-anim-src="([^"]+)"', attrs)
        static = re.search(r'data-static-src="([^"]+)"', attrs)
        title = re.search(r'data-title="([^"]+)"', attrs)
        if not anim:
            return m.group(0)
        src = anim.group(1)
        # Normalise path: _static/gifs/foo.gif → /images/foo
        src = re.sub(r'^.*_static/gifs/', '/images/', src)
        src = re.sub(r'^/_images/', '/images/', src)
        base = re.sub(r'\.(gif|GIF)$', '', src)
        poster = static.group(1) if static else base + '.png'
        poster = re.sub(r'^.*_static/gifs/', '/images/', poster)
        poster = re.sub(r'^/_images/', '/images/', poster)
        alt = title.group(1) if title else ''
        return (
            f'<video autoplay loop muted playsinline poster="{poster}" '
            f'title="{alt}" style="width: 80%; display: block; margin: 1rem 0">'
            f'<source src="{base}.webm" type="video/webm" />'
            f'<source src="{base}.mp4" type="video/mp4" />'
            f'</video>'
        )

    text = re.sub(
        r'<div\s+((?:[^>]*\s)?class="gif-player"[^>]*)/?>(?:</div>)?',
        gif_player_to_video, text
    )

    # 5. Convert :doc: cross-refs left by pandoc as interpreted-text spans.
    #    Simple form:  `slug`{.interpreted-text role="doc"}
    #    Titled form:  `display text <path>`{.interpreted-text role="doc"}
    def doc_ref(m: re.Match) -> str:
        content = m.group(1).strip()
        # Strip blockquote markers ("> ") from multiline content
        content = re.sub(r'\n>\s*', ' ', content).strip()
        titled = re.match(r'^(.+?)\s*<([^>]+)>$', content, re.DOTALL)
        if titled:
            label = titled.group(1).strip()
            path = re.sub(r'^(\.\./)+', '', titled.group(2).strip())
            return f'[{label}](/{path})'
        else:
            slug = re.sub(r'\s+', '-', content)
            label = Path(slug).name
            return f'[{label}](/{slug})'

    text = re.sub(
        r'`([^`]+)`\{\.interpreted-text\s+role="doc"\}',
        doc_ref, text
    )

    # 6. Strip :ref: spans — keep display text only.
    #    Titled form: `display text <label>`{...} → "display text"
    #    Simple form: `label`{...} → "label"
    def ref_label(m: re.Match) -> str:
        content = m.group(1)
        titled = re.match(r'^(.+?)\s*<[^>]+>$', content)
        return titled.group(1).strip() if titled else content

    text = re.sub(r'`([^`]+)`\{\.interpreted-text\s+role="ref"\}', ref_label, text)

    # 7. Add MDX frontmatter if missing
    if not text.startswith('---'):
        heading = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
        title = heading.group(1).strip() if heading else path.stem
        # Escape double quotes in title
        title = title.replace('"', '\\"')
        text = f'---\ntitle: "{title}"\n---\n\n' + text

    # 7b. Strip first H1 — Starlight renders it from frontmatter title
    text = re.sub(r'^(---\n.*?\n---\n+)# [^\n]+\n+', r'\1', text, count=1, flags=re.DOTALL)

    # 7c. Strip stale inline <script> tags left over from Sphinx RST files
    text = re.sub(r'\n?<script[^>]*src="[^"]*_static[^"]*"[^>]*></script>', '', text)

    # 8a. Strip pandoc inline span attributes [text]{.class} → text
    #     and heading ID anchors {#some-id} — MDX treats {} as JSX
    text = re.sub(r'\[([^\]]+)\]\{[^}]+\}', r'\1', text)
    text = re.sub(r'(\s*\{#[^}]+\})', '', text)

    # 8b. Convert bare autolinks <https://url> → [url](url)
    text = re.sub(r'<(https?://[^>]+)>', lambda m: f'[{m.group(1)}]({m.group(1)})', text)

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
