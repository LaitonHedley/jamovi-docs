# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Sphinx documentation for [jamovi](https://www.jamovi.org), a free statistical software application. Published at https://jamovi.readthedocs.org and supports 25+ languages via Weblate translations.

## Build commands

The virtual environment lives in `.venv/` (not `_env` as the README says).

```bash
# Activate the virtual environment
source .venv/bin/activate

# Install dependencies (first time or after updates)
pip install -r requirements.txt

# Build English HTML docs
make html

# Build for a specific language (e.g. German)
make html LANG=de

# Clean the build output
make clean

# Check for broken links
make checklinks

# Live-reload server for local development
sphinx-autobuild . _build/html/en
```

## Project structure

- `index.rst` — master toctree that defines the site's navigation
- `conf.py` — Sphinx configuration
- `usermanual/` — Getting Started guides (`um_*.rst`)
- `analyses/` — Step-by-step analysis walkthroughs (`jg_*.rst`)
- `transformations/` — Data manipulation and transformation docs (`tr_*.rst`)
- `developer/` — Module developer hub (`dh_*.rst`)
- `spss2jamovi/` — SPSS-to-jamovi transition guides (`s2j_*.rst`)
- `jmv/` — R package (`jmv`) API reference (`jmv_*.rst`)
- `howto/` — Short how-to guides
- `_images/` — All images referenced across all docs
- `_locale/` — Git submodule containing translations (from Weblate at https://hosted.weblate.org/projects/jamovidocs/)
- `_static/`, `_templates/` — Sphinx theme customisation
- `.languages` — List of language codes to build when publishing all translations

## File naming conventions

Files are prefixed by section and numbered: `um_4_spreadsheet.rst`, `jg_11_descriptive-analyses.rst`, `dh_tut_13-creating-an-analysis.rst`. New files should follow the same pattern for the section they belong to.

## Working on documentation content

Apply the following expertise automatically whenever writing, editing, reviewing, or discussing RST content in this project — without being asked.

### Audience

Researchers, students, and scientists who want to analyse their data. They chose jamovi because it is approachable. Assume they understand what they want to do statistically, but not how software works. Many have never used a command line.

### Writing style

- **Direct and instructional** — tell the reader exactly what to click, select, or type
- **Second person** — "click the Data tab", "select Append", not "the user should click..."
- **Friendly but not chatty** — no filler phrases, no over-explaining what was just done
- When a statistical concept is necessary, name it plainly and add a `More info <url>__` link where one exists in the existing docs

### RST conventions

- Images: defined as substitutions at the bottom of the file, referenced inline as `|name|`:
  ```rst
  |image_name|

  .. |image_name| image:: ../_images/filename.png
     :alt: Description of the image.
     :class: centered
     :width: 42%
  ```
- Cross-file links: `:doc:` for pages, `:ref:` for labelled anchors
- Tabular examples: `.. list-table::` with `:header-rows: 1`
- Author credit: `.. sectionauthor:: Name` at the top of the file

### Automatic user-perspective review

After producing or substantially modifying documentation content, silently do a user-perspective pass before presenting output. Fix obvious issues; flag anything that requires a judgment call. Specifically check:

- Would a first-time user know exactly what to do at each step? Are steps in the right order?
- Is any jargon or statistical term used without explanation or a link?
- Are there TODO markers, `*link*` placeholders, "WTF" comments, or broken image references still present?
- Does the section heading match the content beneath it?

### Explicit slash commands

For a structured full-page review or a focused writing session, two commands are available in `.claude/commands/`:

- `/review-docs <file>` — structured user-perspective review of a complete page
- `/write-docs <task>` — writing session with full style context loaded

## Workflow

- **Plan before implementing** — for any non-trivial change (new section, page restructure, content rework), propose a plan first and wait for the user to approve it before making edits.
- **Build after rework** — once edits are finalised, run `source .venv/bin/activate && make html` to confirm the docs still build cleanly. Report any warnings or errors before asking the user to review the result.
- **Parallel work** — when asked to work on two or more independent sections or files simultaneously, spawn parallel sub-agents with `isolation: "worktree"`. Each agent must: (1) read `CLAUDE.md` at the start so it has full project context, (2) complete its task, (3) run `source .venv/bin/activate && make html` to verify the build. Report back the branch name, a summary of changes, and build status for each.

## Committing

- **Small logical commits** — break changes into small, focused commits with a single purpose.
- **Commit title** — a single sentence in imperative mood, max 50 characters, no trailing dot, no type prefixes (e.g. no "feat:", "fix:").
- **Optional description** — only to clarify functional choices (the "what" and "why"). Do not explain the "how" or anything already evident from the diff. Max line length 72 characters.
- **No AI mentions** — never mention AI assistants or tools in commit messages.
- **Propose first** — always propose a draft commit message for the user to approve before committing.

## Deployment

ReadTheDocs reads `.readthedocs.yaml` and builds with `conf.py`. The `fail_on_warning: false` setting means warnings won't break the build. PRs pushed to `main` (and the `_locale` submodule) are automatically picked up by ReadTheDocs.
