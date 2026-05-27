# Astro/Starlight Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate the jamovi Sphinx/ReadTheDocs documentation to an Astro Starlight site, preserving all 25 existing translations (gettext .po format) and the Weblate contribution workflow.

**Architecture:** Use Astro Starlight for the site (built-in i18n, sidebar, search, and accessibility). English RST source files are converted to MDX via pandoc + a post-processing script. Translations are kept in the existing `.po` gettext files (submodule `_locale`) and a build-time Python script generates translated MDX files per locale. Starlight routes `/en/`, `/de/`, `/fr/`, … automatically.

**Tech Stack:** Astro 5, `@astrojs/starlight`, Node.js (npm), Python 3 (translation generator script), pandoc (RST→MD conversion), pagefind (search), Weblate (translation management — unchanged).

---

## File / Folder Map

```
jamovi-docs/
├── src/
│   ├── content/
│   │   └── docs/
│   │       ├── usermanual/          ← English MDX (converted from RST)
│   │       ├── analyses/
│   │       ├── data/
│   │       ├── howto/
│   │       ├── spss2jamovi/
│   │       ├── de/                  ← Generated translated MDX (gitignored)
│   │       │   ├── usermanual/
│   │       │   └── ...
│   │       └── fr/ ...              ← One folder per locale
│   └── assets/                      ← Moved from _images/
│       └── *.png / *.svg / ...
├── public/
│   ├── gifs/                        ← Moved from _static/gifs/
│   └── output/                      ← Moved from _static/output/
├── scripts/
│   ├── convert-rst.sh               ← Runs pandoc on all RST files
│   ├── postprocess-mdx.py           ← Fixes image refs, links, RST remnants
│   └── generate-translations.py     ← .po files → translated MDX per locale
├── astro.config.mjs
├── package.json
├── tsconfig.json
└── .gitignore                       ← Add src/content/docs/{de,fr,...}/
```

**Source content directories (RST):** `usermanual/`, `analyses/`, `data/`, `howto/`, `spss2jamovi/` — each RST file maps 1:1 to an MDX file in `src/content/docs/<section>/`.

**Locale submodule:** `_locale/` (git submodule `sjentsch/jamoviDocs-i18n`) — already in repo, needs `git submodule update --init` before the translation step. `.po` files are at `_locale/<lang>/LC_MESSAGES/<section>.po`.

---

## Task 1: Install pandoc

**Files:**
- No code changes — verify tooling

- [ ] **Step 1: Check if pandoc is installed**

```bash
pandoc --version
```

Expected: version 3.x. If missing, install:

```bash
brew install pandoc
```

- [ ] **Step 2: Confirm pandoc can handle RST**

```bash
pandoc usermanual/um_2_first-steps.rst -f rst -t markdown --wrap=none -o /tmp/test.md && head -30 /tmp/test.md
```

Expected: readable Markdown output with headings and prose intact.

---

## Task 2: Scaffold the Astro Starlight project

**Files:**
- Create: `package.json`
- Create: `astro.config.mjs`
- Create: `tsconfig.json`
- Create: `src/content/docs/.gitkeep`

- [ ] **Step 1: Initialize Astro with Starlight in the current repo**

```bash
npm create astro@latest . -- --template starlight --no-install --typescript strict --git false
```

When prompted, accept overwriting only non-conflicting files. If the CLI is interactive, run instead:

```bash
npm init -y && npm install astro @astrojs/starlight
```

Then create `astro.config.mjs` manually (see Step 3).

- [ ] **Step 2: Install dependencies**

```bash
npm install
```

Expected: `node_modules/` created, no errors.

- [ ] **Step 3: Replace `astro.config.mjs` with the full i18n config**

Create `astro.config.mjs`:

```js
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://docs.jamovi.org',
  integrations: [
    starlight({
      title: 'jamovi Documentation',
      logo: {
        src: './src/assets/header-logo.svg',
      },
      favicon: '/jamovi-v.svg',
      defaultLocale: 'root',
      locales: {
        root: { label: 'English', lang: 'en' },
        ar:    { label: 'العربية',             lang: 'ar' },
        da:    { label: 'Dansk',               lang: 'da' },
        de:    { label: 'Deutsch',             lang: 'de' },
        es:    { label: 'Español',             lang: 'es' },
        fi:    { label: 'Suomi',               lang: 'fi' },
        fr:    { label: 'Français',            lang: 'fr' },
        hr:    { label: 'Hrvatski',            lang: 'hr' },
        is:    { label: 'Íslenska',            lang: 'is' },
        it:    { label: 'Italiano',            lang: 'it' },
        ja:    { label: '日本語',               lang: 'ja' },
        ko:    { label: '한국어',               lang: 'ko' },
        nb:    { label: 'Norsk bokmål',        lang: 'nb' },
        nn:    { label: 'Norsk nynorsk',       lang: 'nn' },
        pl:    { label: 'Polski',              lang: 'pl' },
        pt:    { label: 'Português',           lang: 'pt' },
        ru:    { label: 'Русский',             lang: 'ru' },
        si:    { label: 'සිංහල',               lang: 'si' },
        sl:    { label: 'Slovenščina',         lang: 'sl' },
        sv:    { label: 'Svenska',             lang: 'sv' },
        ta:    { label: 'தமிழ்',               lang: 'ta' },
        tr:    { label: 'Türkçe',              lang: 'tr' },
        uk:    { label: 'Українська',          lang: 'uk' },
        vi:    { label: 'Tiếng Việt',          lang: 'vi' },
        zh_CN: { label: '简体中文',             lang: 'zh-CN' },
        zh_TW: { label: '繁體中文',             lang: 'zh-TW' },
      },
      sidebar: [
        {
          label: 'Getting Started',
          autogenerate: { directory: 'usermanual' },
        },
        {
          label: 'Analyses',
          autogenerate: { directory: 'analyses' },
        },
        {
          label: 'Data Handling',
          autogenerate: { directory: 'data' },
        },
        {
          label: 'How to…',
          autogenerate: { directory: 'howto' },
        },
        {
          label: 'From SPSS to jamovi',
          autogenerate: { directory: 'spss2jamovi' },
        },
      ],
      customCss: ['./src/styles/jamovi.css'],
      social: {
        github: 'https://github.com/jamovi/jamovi',
      },
    }),
  ],
});
```

- [ ] **Step 4: Create the custom CSS stub**

```bash
mkdir -p src/styles
```

Create `src/styles/jamovi.css`:

```css
/* jamovi brand overrides — expand later */
:root {
  --sl-color-accent: #2d7dd2;
  --sl-color-accent-high: #1a5fa8;
}
```

- [ ] **Step 5: Create `src/assets/` and copy logo files**

```bash
mkdir -p src/assets
cp _images/header-logo.svg src/assets/
cp _images/jamovi-v.svg public/
```

- [ ] **Step 6: Verify the dev server starts**

```bash
npm run dev
```

Expected: server at http://localhost:4321 with a bare Starlight site. No build errors.

- [ ] **Step 7: Commit**

```bash
git add package.json package-lock.json astro.config.mjs tsconfig.json src/ public/
git commit -m "Scaffold Astro Starlight project with i18n config"
```

---

## Task 3: Set up asset directories

**Files:**
- Create: `src/assets/` (images referenced from MDX)
- Create: `public/gifs/`, `public/output/`, `public/syntax/`, `public/fonts/`

- [ ] **Step 1: Copy images to `src/assets/`**

```bash
cp _images/*.png _images/*.jpg _images/*.svg src/assets/ 2>/dev/null; true
```

- [ ] **Step 2: Copy public static files**

```bash
mkdir -p public/gifs public/output public/syntax public/fonts
cp _static/gifs/* public/gifs/
cp _static/output/* public/output/
cp _static/syntax/* public/syntax/
cp _static/fonts/* public/fonts/
cp _static/gif-player.js public/
```

- [ ] **Step 3: Add gif-player script to Starlight head**

In `astro.config.mjs`, inside the `starlight({})` call, add:

```js
head: [
  {
    tag: 'script',
    attrs: { src: '/gif-player.js', defer: true },
  },
],
```

- [ ] **Step 4: Commit**

```bash
git add src/assets/ public/
git commit -m "Add images and static assets"
```

---

## Task 4: Write the RST → MDX conversion script

**Files:**
- Create: `scripts/convert-rst.sh`
- Create: `scripts/postprocess-mdx.py`

This is the most complex task. Pandoc handles basic RST → Markdown but several Sphinx-specific patterns need custom post-processing.

**RST patterns that need post-processing:**
1. Image substitutions like `.. |name| image:: ../_images/foo.png` + `|name|` usage → inline `![](../../assets/foo.png)` or `<img>`
2. `:width:` / `:align:` image options → inline `style` attributes
3. `.. note::` / `.. warning::` → Starlight `:::note` / `:::caution` asides
4. `:doc:\`path\`` cross-references → relative `.mdx` links
5. `.. sectionauthor::` directives → frontmatter `author:` or drop
6. `.. toctree::` blocks → drop (Starlight uses sidebar config)
7. `_images/` path prefix → `../../assets/` or `/` depending on location

- [ ] **Step 1: Create the shell conversion script**

Create `scripts/convert-rst.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

SECTIONS=(usermanual analyses data howto spss2jamovi)
OUTBASE="src/content/docs"

for section in "${SECTIONS[@]}"; do
  mkdir -p "${OUTBASE}/${section}"
  for rst in "${section}"/*.rst; do
    [ -f "$rst" ] || continue
    base=$(basename "$rst" .rst)
    out="${OUTBASE}/${section}/${base}.mdx"
    pandoc "$rst" \
      -f rst \
      -t markdown \
      --wrap=none \
      --markdown-headings=atx \
      -o "$out"
    echo "Converted: $rst → $out"
  done
done
echo "Done. Run scripts/postprocess-mdx.py next."
```

```bash
chmod +x scripts/convert-rst.sh
```

- [ ] **Step 2: Run the conversion to see raw pandoc output**

```bash
bash scripts/convert-rst.sh
```

Expected: `.mdx` files in each `src/content/docs/<section>/` directory.

- [ ] **Step 3: Inspect the output and note patterns to fix**

```bash
head -60 src/content/docs/usermanual/um_2_first-steps.mdx
grep -r '|.*|' src/content/docs/ | head -20
grep -r '_images/' src/content/docs/ | head -20
grep -r '\.\. note' src/content/docs/ | head -10
```

Note which patterns appear — this guides the post-processor.

- [ ] **Step 4: Create `scripts/postprocess-mdx.py`**

Create `scripts/postprocess-mdx.py`:

```python
#!/usr/bin/env python3
"""Post-process pandoc-converted MDX files to fix Sphinx-specific patterns."""
import re
import sys
from pathlib import Path

DOCS_DIR = Path("src/content/docs")


def extract_substitutions(text: str) -> dict[str, dict]:
    """Parse RST substitution definitions that pandoc leaves behind."""
    subs = {}
    # Pattern: .. |name| image:: path\n   :width: X\n   :align: Y
    pattern = re.compile(
        r'\.\.\s+\|(\w+)\|\s+image::\s+(\S+)((?:\n\s+:\w+:[^\n]*)*)',
        re.MULTILINE
    )
    for m in pattern.finditer(text):
        name, path, opts_raw = m.group(1), m.group(2), m.group(3)
        opts = {}
        for opt in re.finditer(r':(\w+):\s*(\S+)', opts_raw):
            opts[opt.group(1)] = opt.group(2)
        subs[name] = {'path': path, 'opts': opts}
    return subs


def fix_image_path(path: str) -> str:
    """Convert _images/ relative paths to src/assets references."""
    path = re.sub(r'^\.\./_images/', '/src/assets/', path)
    path = re.sub(r'^_images/', '/src/assets/', path)
    return path


def sub_to_img(name: str, info: dict) -> str:
    """Convert a substitution definition to an MDX img tag."""
    path = fix_image_path(info['path'])
    opts = info.get('opts', {})
    style_parts = []
    if 'width' in opts:
        w = opts['width']
        style_parts.append(f'width:{w}')
    style = '; '.join(style_parts)
    alt = name.replace('_', ' ')
    if style:
        return f'<img src="{path}" alt="{alt}" style="{style}" />'
    return f'![{alt}]({path})'


def process_file(path: Path) -> None:
    text = path.read_text(encoding='utf-8')

    # 1. Extract substitution definitions before removing them
    subs = extract_substitutions(text)

    # 2. Remove toctree blocks (pandoc may leave them as raw RST)
    text = re.sub(
        r'\.\.\s+toctree::.*?(?=\n\S|\Z)', '', text, flags=re.DOTALL
    )

    # 3. Remove sectionauthor directives
    text = re.sub(r'\.\.\s+sectionauthor::[^\n]*\n?', '', text)

    # 4. Remove substitution definition lines
    text = re.sub(
        r'\.\.\s+\|\w+\|\s+image::.*?(?=\n\S|\n\n|\Z)',
        '', text, flags=re.DOTALL
    )

    # 5. Replace |name| usage with img tags
    for name, info in subs.items():
        text = text.replace(f'|{name}|', sub_to_img(name, info))

    # 6. Fix bare _images/ paths in any remaining markdown image syntax
    text = re.sub(r'!\[([^\]]*)\]\(\.\./+_images/([^)]+)\)',
                  lambda m: f'![{m.group(1)}](/src/assets/{m.group(2)})', text)
    text = re.sub(r'!\[([^\]]*)\]\(_images/([^)]+)\)',
                  lambda m: f'![{m.group(1)}](/src/assets/{m.group(2)})', text)

    # 7. Convert RST note/warning/tip blocks
    def convert_aside(m):
        kind_map = {'note': 'note', 'warning': 'caution', 'tip': 'tip',
                    'important': 'danger', 'hint': 'tip'}
        kind = kind_map.get(m.group(1).lower(), 'note')
        body = re.sub(r'\n   ', '\n', m.group(2)).strip()
        return f':::{{.{kind}}}\n{body}\n:::'

    text = re.sub(
        r'\.\.\s+(note|warning|tip|important|hint)::\n((?:\n   [^\n]*|\n)+)',
        convert_aside, text, flags=re.IGNORECASE
    )

    # 8. Convert :doc:`path` cross-refs to relative .mdx links
    text = re.sub(
        r':doc:`([^`]+)`',
        lambda m: f'[{Path(m.group(1)).name}]({m.group(1)}.mdx)', text
    )

    # 9. Convert :ref:`label` to plain text (can be refined later)
    text = re.sub(r':ref:`([^`]+)`', r'\1', text)

    # 10. Add MDX frontmatter if missing
    if not text.startswith('---'):
        # Extract first heading as title
        heading_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
        title = heading_match.group(1) if heading_match else path.stem
        text = f'---\ntitle: "{title}"\n---\n\n' + text

    # 11. Strip excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    path.write_text(text.strip() + '\n', encoding='utf-8')
    print(f'Processed: {path}')


def main():
    mdx_files = list(DOCS_DIR.glob('**/*.mdx'))
    # Skip locale subdirs (only process root English content)
    mdx_files = [f for f in mdx_files if not any(
        part in ('de', 'fr', 'es', 'ar', 'da', 'fi', 'hr', 'is', 'it',
                 'ja', 'ko', 'nb', 'nn', 'pl', 'pt', 'ru', 'si', 'sl',
                 'sv', 'ta', 'tr', 'uk', 'vi', 'zh_CN', 'zh_TW')
        for part in f.parts
    )]
    for f in mdx_files:
        process_file(f)
    print(f'\nDone. Processed {len(mdx_files)} files.')


if __name__ == '__main__':
    main()
```

- [ ] **Step 5: Run the post-processor**

```bash
python3 scripts/postprocess-mdx.py
```

Expected: all MDX files updated, no Python errors.

- [ ] **Step 6: Spot-check the output**

```bash
head -40 src/content/docs/usermanual/um_2_first-steps.mdx
head -40 src/content/docs/data/data_1_overview_data_variables.mdx
```

Check that: frontmatter has `title:`, images use `/src/assets/` paths, no leftover `.. toctree` blocks.

- [ ] **Step 7: Check dev server renders content**

```bash
npm run dev
```

Open http://localhost:4321 and click through a few pages. Images may be broken at this point (we'll fix in Task 5) but prose should render.

- [ ] **Step 8: Commit**

```bash
git add scripts/ src/content/docs/
git commit -m "Convert English RST content to MDX"
```

---

## Task 5: Fix images in MDX (Starlight asset pipeline)

**Files:**
- Modify: `astro.config.mjs` (if needed)
- Modify: MDX files with remaining broken image paths

Starlight serves images from `src/assets/` via Astro's image optimization pipeline (referenced as `~/assets/...`) OR from `public/` as static paths. Since these are documentation screenshots (not needing optimization), the simplest approach is `public/images/`.

- [ ] **Step 1: Move images to `public/images/`**

```bash
mkdir -p public/images
cp _images/*.png _images/*.jpg _images/*.svg public/images/ 2>/dev/null; true
cp _static/gifs/*.gif _static/gifs/*.png public/images/ 2>/dev/null; true
```

- [ ] **Step 2: Update image paths in all MDX files**

```bash
find src/content/docs -name '*.mdx' -exec sed -i '' 's|/src/assets/|/images/|g' {} +
find src/content/docs -name '*.mdx' -exec sed -i '' 's|src="/src/assets/|src="/images/|g' {} +
```

- [ ] **Step 3: Check images load in the browser**

```bash
npm run dev
```

Navigate to http://localhost:4321/usermanual/um_2_first-steps and verify the screenshot images appear.

- [ ] **Step 4: Commit**

```bash
git add public/images/ src/content/docs/
git commit -m "Fix image paths to use public/images/"
```

---

## Task 6: Refine the sidebar navigation

The `autogenerate` sidebar in Task 2 picks up all files alphabetically. The current site has a specific ordering. This task locks in the correct order using Starlight's explicit sidebar config.

**Files:**
- Modify: `astro.config.mjs`

- [ ] **Step 1: Replace autogenerate entries with explicit ordered lists**

In `astro.config.mjs`, replace the `sidebar` array with:

```js
sidebar: [
  {
    label: 'Getting Started',
    items: [
      { slug: 'usermanual/um_1_installation' },
      { slug: 'usermanual/um_2_first-steps' },
      { slug: 'usermanual/um_3_analyses' },
      { slug: 'usermanual/um_4_spreadsheet' },
      { slug: 'usermanual/um_5_updating_data' },
      { slug: 'usermanual/um_6_jamovi_and_R' },
    ],
  },
  {
    label: 'Analyses',
    items: [
      { slug: 'analyses/jg_overview' },
    ],
  },
  {
    label: 'Data Handling',
    items: [
      { slug: 'data/data_overview' },
      { slug: 'data/data_1_overview_data_variables' },
      { slug: 'data/data_2_computed_variables' },
      { slug: 'data/data_3_transformed_variables' },
      { slug: 'data/data_6_filtering_data' },
      { slug: 'data/data_4_row_v_functions' },
      { slug: 'data/data_5_list_of_functions' },
      { slug: 'data/data_7_restructure_data' },
      { slug: 'data/data_8_common_data_recipes' },
      { slug: 'data/data_9_date_handling' },
    ],
  },
  {
    label: 'How to…',
    items: [
      { slug: 'howto/howto_overview' },
      { slug: 'howto/howto_Filtering_data' },
      { slug: 'howto/howto_Install_modules' },
      { slug: 'howto/howto_Use_PROCESS' },
    ],
  },
  {
    label: 'From SPSS to jamovi',
    items: [
      { slug: 'spss2jamovi/s2j_Comparison_of_analyses' },
      { slug: 'spss2jamovi/s2j_side-by-side' },
    ],
  },
],
```

- [ ] **Step 2: Verify sidebar order in the browser**

```bash
npm run dev
```

Check http://localhost:4321 — sidebar should match the original ReadTheDocs structure.

- [ ] **Step 3: Commit**

```bash
git add astro.config.mjs
git commit -m "Set explicit sidebar navigation order"
```

---

## Task 7: Write the translation generator script

This is the heart of the i18n migration. The script reads `.po` files from `_locale/<lang>/LC_MESSAGES/<section>.po` and generates translated MDX files in `src/content/docs/<lang>/`.

**Files:**
- Create: `scripts/generate-translations.py`
- Modify: `.gitignore` (add translated locale dirs)

**How it works:** Each `.po` file maps `msgid` (English paragraph) → `msgstr` (translation). The script:
1. Loads all msgid→msgstr pairs from the `.po` file
2. Reads the English MDX file
3. Replaces English text blocks with their translations (paragraph-by-paragraph)
4. Writes the result to `src/content/docs/<lang>/<section>/<file>.mdx`

**Important:** We use `python-polib` to parse `.po` files properly (handles multiline msgids, escape sequences, etc.).

- [ ] **Step 1: Install polib**

```bash
pip install polib
```

Or add to requirements:

```bash
echo "polib>=1.2.0" >> requirements.txt
pip install -r requirements.txt
```

- [ ] **Step 2: Initialize the locale submodule**

```bash
git submodule update --init _locale
ls _locale/de/LC_MESSAGES/
```

Expected: `analyses.po`, `howto.po`, `index.po`, `sphinx.po`, `spss2jamovi.po`, `usermanual.po`

- [ ] **Step 3: Create `scripts/generate-translations.py`**

Create `scripts/generate-translations.py`:

```python
#!/usr/bin/env python3
"""
Generate translated MDX files from .po translation files.

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

# Map section directory names to the .po file base name
SECTION_TO_PO = {
    "usermanual":  "usermanual",
    "analyses":    "analyses",
    "data":        "usermanual",   # data pages live in the usermanual .po
    "howto":       "howto",
    "spss2jamovi": "spss2jamovi",
}


def load_po(lang: str, po_name: str) -> dict[str, str]:
    """Return msgid→msgstr dict for a given language and .po file."""
    po_path = LOCALE_DIR / lang / "LC_MESSAGES" / f"{po_name}.po"
    if not po_path.exists():
        return {}
    po = polib.pofile(str(po_path))
    return {entry.msgid: entry.msgstr for entry in po if entry.msgstr}


def translate_block(text: str, translations: dict[str, str]) -> str:
    """
    Replace paragraphs/headings in `text` with their translations.
    We do exact-match replacement on paragraphs — works well for
    documentation prose where each paragraph is a discrete msgid.
    """
    if not translations:
        return text

    # Split into paragraphs (double newline boundaries)
    # Process each paragraph independently
    paragraphs = re.split(r'(\n\n+)', text)
    result = []
    for chunk in paragraphs:
        stripped = chunk.strip()
        if stripped in translations and translations[stripped]:
            # Preserve surrounding whitespace structure
            result.append(chunk.replace(stripped, translations[stripped]))
        else:
            result.append(chunk)
    return ''.join(result)


def translate_frontmatter_title(text: str, translations: dict[str, str]) -> str:
    """Translate the title: field in frontmatter if a translation exists."""
    def replace_title(m):
        title = m.group(1)
        translated = translations.get(title, title)
        return f'title: "{translated}"'
    return re.sub(r'title:\s+"([^"]+)"', replace_title, text)


def process_file(
    src_path: Path,
    dest_path: Path,
    translations: dict[str, str],
) -> None:
    text = src_path.read_text(encoding='utf-8')
    text = translate_frontmatter_title(text, translations)

    # Separate frontmatter from body
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            frontmatter = '---' + parts[1] + '---'
            body = parts[2]
            body = translate_block(body, translations)
            text = frontmatter + body
        else:
            text = translate_block(text, translations)
    else:
        text = translate_block(text, translations)

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(text, encoding='utf-8')


def get_all_languages() -> list[str]:
    if LANGUAGES_FILE.exists():
        langs = [l.strip() for l in LANGUAGES_FILE.read_text().splitlines()
                 if l.strip() and l.strip() != 'en']
        return langs
    return [d.name for d in LOCALE_DIR.iterdir()
            if d.is_dir() and d.name != 'pot']


def main():
    langs = sys.argv[1:] if len(sys.argv) > 1 else get_all_languages()

    # Collect all English source MDX files grouped by section
    sections = [d for d in DOCS_DIR.iterdir()
                if d.is_dir() and d.name in SECTION_TO_PO]

    for lang in langs:
        po_cache: dict[str, dict[str, str]] = {}

        for section_dir in sections:
            po_name = SECTION_TO_PO[section_dir.name]
            if po_name not in po_cache:
                po_cache[po_name] = load_po(lang, po_name)
            translations = po_cache[po_name]

            for src_file in section_dir.glob('*.mdx'):
                dest_file = DOCS_DIR / lang / section_dir.name / src_file.name
                process_file(src_file, dest_file, translations)

        print(f"Generated: {lang}")

    print("Done.")


if __name__ == '__main__':
    main()
```

- [ ] **Step 4: Add generated locale dirs to `.gitignore`**

Append to `.gitignore`:

```
# Generated translated MDX (built from _locale .po files)
src/content/docs/ar/
src/content/docs/da/
src/content/docs/de/
src/content/docs/es/
src/content/docs/fi/
src/content/docs/fr/
src/content/docs/hr/
src/content/docs/is/
src/content/docs/it/
src/content/docs/ja/
src/content/docs/ko/
src/content/docs/nb/
src/content/docs/nn/
src/content/docs/pl/
src/content/docs/pt/
src/content/docs/ru/
src/content/docs/si/
src/content/docs/sl/
src/content/docs/sv/
src/content/docs/ta/
src/content/docs/tr/
src/content/docs/uk/
src/content/docs/vi/
src/content/docs/zh_CN/
src/content/docs/zh_TW/
```

- [ ] **Step 5: Run for one language to test**

```bash
python3 scripts/generate-translations.py de
ls src/content/docs/de/usermanual/
head -40 src/content/docs/de/usermanual/um_2_first-steps.mdx
```

Expected: German content where translations exist; English fallback where `msgstr` is empty.

- [ ] **Step 6: Commit**

```bash
git add scripts/generate-translations.py requirements.txt .gitignore
git commit -m "Add translation generator script for .po → MDX"
```

---

## Task 8: Run full translation generation and test i18n

**Files:**
- `src/content/docs/<lang>/` (generated, gitignored)

- [ ] **Step 1: Generate all locales**

```bash
python3 scripts/generate-translations.py
```

Expected: 25 language directories created under `src/content/docs/`.

- [ ] **Step 2: Start dev server and test language switching**

```bash
npm run dev
```

Navigate to:
- http://localhost:4321/ (English)
- http://localhost:4321/de/ (German)
- http://localhost:4321/fr/ (French)

Check: language switcher in header/footer shows all 25 languages. Pages in German show translated content where available.

- [ ] **Step 3: Verify untranslated pages fall back to English**

Navigate to a page that has no German translation (an empty `msgstr`). Starlight should show the English version with a "This page is not yet translated" banner (Starlight built-in behaviour).

- [ ] **Step 4: Fix any broken routes**

If any page 404s, check the frontmatter `title:` is present and the file path matches the sidebar slug. Fix individually as needed.

- [ ] **Step 5: Commit**

```bash
git add scripts/ requirements.txt
git commit -m "Wire up full i18n generation for all 25 locales"
```

---

## Task 9: Build verification and cleanup

**Files:**
- Modify: `package.json` (add `prebuild` script)
- Modify: `.readthedocs.yaml` (or delete)

- [ ] **Step 1: Add a `prebuild` npm script that generates translations**

In `package.json`, update the `scripts` section:

```json
"scripts": {
  "dev": "astro dev",
  "build": "npm run generate-translations && astro build",
  "generate-translations": "git submodule update --init _locale && python3 scripts/generate-translations.py",
  "preview": "astro preview",
  "astro": "astro"
}
```

- [ ] **Step 2: Run a production build**

```bash
npm run build
```

Expected: `dist/` directory created. Watch for any MDX parse errors — fix them in the relevant `.mdx` file by escaping `{`, `}`, `<` characters that MDX treats as JSX.

Fix MDX escaping issues (common with RST content):

```bash
# Find files with unescaped curly braces outside code blocks
grep -rn '{[^{]' src/content/docs/*.mdx src/content/docs/**/*.mdx 2>/dev/null | grep -v '```' | head -20
```

For each flagged file, escape bare `{` → `\{` and `}` → `\}` in prose (not in code fences).

- [ ] **Step 3: Preview the production build**

```bash
npm run preview
```

Open http://localhost:4321 and check the main sections work correctly.

- [ ] **Step 4: Remove obsolete ReadTheDocs config**

The `.readthedocs.yaml` and Sphinx config (`conf.py`, `requirements.txt` Sphinx entries) can be archived but not deleted yet — keep them on the branch until deployment is confirmed working.

Add a comment to `.readthedocs.yaml`:

```yaml
# This file is preserved for reference during the Astro migration.
# The new site uses Astro Starlight — see astro.config.mjs.
```

- [ ] **Step 5: Final commit**

```bash
git add package.json
git commit -m "Add prebuild translation generation to npm build script"
```

---

## Task 10: Deployment configuration

**Files:**
- Create: `netlify.toml` (or `.github/workflows/deploy.yml` for GitHub Pages)

The current site is on ReadTheDocs. Astro Starlight works well on Netlify or GitHub Pages (static output).

- [ ] **Step 1: Choose deployment target**

Decide between Netlify or GitHub Pages. For Netlify:

Create `netlify.toml`:

```toml
[build]
  command = "npm run build"
  publish = "dist"

[build.environment]
  NODE_VERSION = "20"
  PYTHON_VERSION = "3.11"

[[redirects]]
  from = "/en/*"
  to = "/:splat"
  status = 301
```

For GitHub Pages (alternative), create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: recursive
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install polib
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist/
  deploy:
    needs: build
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
    runs-on: ubuntu-latest
    steps:
      - uses: actions/deploy-pages@v4
```

- [ ] **Step 2: Commit deployment config**

```bash
git add netlify.toml   # or .github/workflows/deploy.yml
git commit -m "Add deployment configuration"
```

- [ ] **Step 3: Push the feature branch**

```bash
git push -u origin feature/astro-migration
```

---

## Self-Review

**Spec coverage check:**
- ✅ Astro + Starlight scaffold with all 26 locales configured
- ✅ RST → MDX conversion (pandoc + post-processor)
- ✅ English content migrated to `src/content/docs/`
- ✅ All 25 non-English locales generated from existing `.po` files
- ✅ Images moved to `public/images/`
- ✅ Sidebar navigation matching current ReadTheDocs structure
- ✅ Weblate workflow preserved (translators continue editing `.po` files)
- ✅ Build script wires `.po` → MDX generation automatically
- ✅ Deployment config

**Known gaps / follow-up work (not in scope for this plan):**
- The `jmv/` section (R package docs) and `analyses/jg_*` detail pages are referenced in the sidebar config above but their RST files were not listed in index.rst toctree. Include them in the convert script if needed.
- GIF player script integration with Starlight MDX — may need a custom Astro component wrapper.
- Weblate pointing: after migration is live, update Weblate to point to the new repo/branch so translators can continue working.
- Math rendering: current site uses MathJax; Starlight supports `remark-math` + `rehype-katex` — add if math blocks appear in content.
