#!/usr/bin/env python3
"""
Generate translated MDX files from .po translation files.

Reads _locale/<lang>/LC_MESSAGES/<section>.po and writes translated MDX
files to src/content/docs/<lang>/<section>/<file>.mdx.

Usage:
  python3 scripts/generate-translations.py          # all locales
  python3 scripts/generate-translations.py de fr    # specific locales
"""
import re
import sys
from pathlib import Path

import polib

LOCALE_DIR = Path("_locale")
DOCS_DIR = Path("src/content/docs")
LANGUAGES_FILE = Path(".languages")

# Maps content section directory → .po file base name
SECTION_TO_PO: dict[str, str] = {
    "usermanual":  "usermanual",
    "analyses":    "analyses",
    "data":        "usermanual",  # data pages share the usermanual .po
    "howto":       "howto",
    "spss2jamovi": "spss2jamovi",
}


def load_po(lang: str, po_name: str) -> dict[str, str]:
    po_path = LOCALE_DIR / lang / "LC_MESSAGES" / f"{po_name}.po"
    if not po_path.exists():
        return {}
    po = polib.pofile(str(po_path))
    return {entry.msgid: entry.msgstr for entry in po if entry.msgstr}


def translate_block(text: str, translations: dict[str, str]) -> str:
    """Replace paragraphs in text with their translations (exact-match).

    Handles both plain paragraphs and blockquote lines (> text) produced by
    pandoc when RST content was indented. Since pandoc is run with --wrap=none
    each paragraph stays on a single line, so line-by-line matching works.
    """
    if not translations:
        return text

    # Pass 1 — translate blockquote text lines (> content)
    # Skip lines that are images or empty blockquote markers.
    def translate_bq_line(m: re.Match) -> str:
        content = m.group(1)
        return '> ' + translations.get(content, content)

    text = re.sub(
        r'^> ([^<\n].+)$',
        translate_bq_line,
        text,
        flags=re.MULTILINE,
    )

    # Pass 2 — translate regular (non-blockquote) paragraphs
    paragraphs = re.split(r'(\n\n+)', text)
    result = []
    for chunk in paragraphs:
        stripped = chunk.strip()
        if stripped and not stripped.startswith('>') and stripped in translations:
            result.append(chunk.replace(stripped, translations[stripped]))
        else:
            result.append(chunk)
    return ''.join(result)


def translate_frontmatter_title(text: str, translations: dict[str, str]) -> str:
    def replace_title(m: re.Match) -> str:
        title = m.group(1)
        return f'title: "{translations.get(title, title)}"'
    return re.sub(r'title:\s+"([^"]+)"', replace_title, text)


def process_file(src: Path, dest: Path, translations: dict[str, str]) -> None:
    text = src.read_text(encoding='utf-8')
    text = translate_frontmatter_title(text, translations)

    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            body = translate_block(parts[2], translations)
            text = '---' + parts[1] + '---' + body
        else:
            text = translate_block(text, translations)
    else:
        text = translate_block(text, translations)

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding='utf-8')


def get_all_languages() -> list[str]:
    if LANGUAGES_FILE.exists():
        return [
            ln.strip() for ln in LANGUAGES_FILE.read_text().splitlines()
            if ln.strip() and ln.strip() != 'en'
        ]
    return [d.name for d in LOCALE_DIR.iterdir() if d.is_dir() and d.name != 'pot']


def main() -> None:
    langs = sys.argv[1:] if len(sys.argv) > 1 else get_all_languages()
    sections = [d for d in DOCS_DIR.iterdir() if d.is_dir() and d.name in SECTION_TO_PO]

    for lang in langs:
        po_cache: dict[str, dict[str, str]] = {}
        file_count = 0

        for section_dir in sections:
            po_name = SECTION_TO_PO[section_dir.name]
            if po_name not in po_cache:
                po_cache[po_name] = load_po(lang, po_name)
            translations = po_cache[po_name]

            for src_file in sorted(section_dir.glob('*.mdx')):
                dest = DOCS_DIR / lang / section_dir.name / src_file.name
                process_file(src_file, dest, translations)
                file_count += 1

        print(f"  {lang}: {file_count} files")

    print("Done.")


if __name__ == '__main__':
    main()
