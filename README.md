# jamovi Documentation

Documentation for [jamovi](https://www.jamovi.org), a free statistical software application. Published at [docs.jamovi.org](https://docs.jamovi.org) and supports 25+ languages via Weblate translations.

Built with [Astro Starlight](https://starlight.astro.build/).

---

## Development

### Prerequisites

- Node.js 18+
- Python 3.10+ (for translation generation only)

### Install dependencies

```bash
npm install
```

### Start the dev server

```bash
npm run dev
```

The site is available at http://localhost:4321.

### Build for production

```bash
npm run build
```

### Preview the production build

```bash
npm run preview
```

---

## Project structure

```
astro.config.mjs        Site configuration and sidebar navigation
src/
  assets/               Logo and other built-in assets
  components/           Custom Astro component overrides
  content/docs/         Page content (MDX files, one per language)
  styles/               Custom CSS
public/
  images/               All images and converted GIFs (as WebM/MP4)
  output/               Downloadable data files (.omv, .spv)
  fonts/                Web fonts
scripts/                Build and conversion scripts
_images/                Original source images (used by RST source files)
_locale/                Git submodule — Weblate translation PO files
rst/                    RST source files
  analyses/             Analysis walkthroughs
  data/                 Data handling guides
  howto/                How-to guides
  jmv/                  jmv R package reference
  spss2jamovi/          SPSS-to-jamovi guides
  usermanual/           Getting started guides
```

The RST files are the canonical source material. The MDX files under `src/content/docs/` are converted from them using the scripts described below.

---

## Content

### Editing existing pages

Edit the MDX files directly in `src/content/docs/`. The dev server hot-reloads on save.

### Converting RST source to MDX

If changes are made to the RST source files, re-run the conversion:

```bash
# Convert all RST files to MDX (requires pandoc)
npm run convert

# Or run stages separately:
npm run convert:rst    # pandoc RST → MDX
npm run convert:post   # post-process MDX (fix images, links, asides, etc.)
```

### Converting GIFs to video

```bash
npm run convert:gifs   # requires ffmpeg
```

---

## Translations

Translations are managed via [Weblate](https://hosted.weblate.org/projects/jamovidocs/) and stored in the `_locale` git submodule.

### Generate translated MDX

```bash
npm run generate-translations
```

This updates the `_locale` submodule and generates translated MDX files under `src/content/docs/<lang>/`. These generated files are git-ignored and rebuilt at deploy time.

### Contributing a translation

Visit [hosted.weblate.org/engage/jamovidocs](https://hosted.weblate.org/engage/jamovidocs/) to get involved.

<a href="https://hosted.weblate.org/engage/jamovidocs/">
<img src="https://hosted.weblate.org/widgets/jamovidocs/-/multi-auto.svg" alt="Translation status" />
</a>

We are grateful to the [Weblate team](https://weblate.org/) who host libre projects free of charge.
