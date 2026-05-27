# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Documentation for [jamovi](https://www.jamovi.org), a free statistical software application. Built with [Astro Starlight](https://starlight.astro.build/) and published at [docs.jamovi.org](https://docs.jamovi.org). Supports 25+ languages via Weblate translations.

## Build commands

```bash
# Install dependencies
npm install

# Start dev server (hot-reload)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Convert RST source files to MDX (requires pandoc)
npm run convert

# Generate translated MDX from _locale submodule
npm run generate-translations
```

## Project structure

- `astro.config.mjs` — site config: logo, locales, sidebar navigation
- `src/content/docs/` — page content as MDX files (one per page per language)
- `src/components/` — custom Astro component overrides (currently: `SiteTitle.astro`)
- `src/styles/jamovi.css` — custom CSS overrides
- `src/assets/` — logo and built-in assets
- `public/images/` — all images and converted animations (WebM/MP4/PNG)
- `public/output/` — downloadable data files (.omv, .spv)
- `public/fonts/` — web fonts
- `scripts/` — RST→MDX conversion and translation generation scripts
- `_images/` — original source images (referenced by RST source files)
- `_locale/` — git submodule with Weblate translation PO files
- `rst/` — RST source files (`analyses/`, `data/`, `howto/`, `spss2jamovi/`, `usermanual/`, `jmv/`)

## File naming conventions

MDX files mirror the RST source names, lowercased: `um_4_spreadsheet.mdx`, `jg_11_descriptive-analyses.mdx`, `s2j_correlation.mdx`. Adding new pages: place the MDX in the correct `src/content/docs/` subdirectory and add a `{ slug: '...' }` entry to the sidebar in `astro.config.mjs`.

## Working on documentation content

Apply the following expertise automatically whenever writing, editing, reviewing, or discussing MDX content in this project — without being asked.

### Audience

Researchers, students, and scientists who want to analyse their data. They chose jamovi because it is approachable. Assume they understand what they want to do statistically, but not how software works. Many have never used a command line.

### Writing style

- **Direct and instructional** — tell the reader exactly what to click, select, or type
- **Second person** — "click the Data tab", "select Append", not "the user should click..."
- **Friendly but not chatty** — no filler phrases, no over-explaining what was just done
- When a statistical concept is necessary, name it plainly and add a link where relevant

### MDX conventions

- Images: use standard Markdown `![alt](/images/filename.png)` or `<img>` for sized images
- Cross-page links: absolute paths from root, e.g. `[page title](/data/data_2_computed_variables)`
- Asides (notes/warnings): Starlight syntax `:::note`, `:::caution`, `:::tip`, `:::danger`
- Downloadable files: link to `/output/filename.omv`

### Automatic user-perspective review

After producing or substantially modifying documentation content, silently do a user-perspective pass before presenting output. Fix obvious issues; flag anything that requires a judgment call. Specifically check:

- Would a first-time user know exactly what to do at each step? Are steps in the right order?
- Is any jargon or statistical term used without explanation or a link?
- Are there TODO markers, placeholder text, or broken image/link references still present?
- Does the section heading match the content beneath it?

### Explicit slash commands

- `/review-docs <file>` — structured user-perspective review of a complete page
- `/write-docs <task>` — writing session with full style context loaded
- `/parallel-docs <tasks>` — coordinate work across multiple independent sections

## Workflow

- **Plan before implementing** — for any non-trivial change (new section, page restructure, content rework), propose a plan first and wait for the user to approve it before making edits.
- **Build after rework** — once edits are finalised, run `npm run build` to confirm the site still builds cleanly. Report any errors before asking the user to review the result.
- **Parallel work** — when asked to work on two or more independent sections or files simultaneously, spawn parallel sub-agents with `isolation: "worktree"`. Each agent must: (1) read `CLAUDE.md` at the start, (2) complete its task, (3) run `npm run build` to verify. Report back the branch name, a summary of changes, and build status for each.

## Committing

- **Small logical commits** — break changes into small, focused commits with a single purpose.
- **Commit title** — a single sentence in imperative mood, max 50 characters, no trailing dot, no type prefixes (e.g. no "feat:", "fix:").
- **Optional description** — only to clarify functional choices. Do not explain the "how" or anything already evident from the diff. Max line length 72 characters.
- **No AI mentions** — never mention AI assistants or tools in commit messages.
- **Propose first** — always propose a draft commit message for the user to approve before committing.
