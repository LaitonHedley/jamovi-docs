# jamovi Docs — Vision Brief

A high-level vision for the jamovi documentation site at docs.jamovi.org.
Intended as an onboarding document for a new developer/content owner.

For day-to-day writing style, MDX conventions, and workflow guidelines, see
`CLAUDE.md` in the root of the repository — that is the authoritative
reference for how to write and work in this codebase.

---

## Vision

jamovi docs should be the definitive, approachable reference for anyone using
jamovi — from a student opening it for the first time, to a researcher who
knows their statistics but is new to the software, to an experienced user who
just needs a reminder of where something lives. The docs are direct and
task-oriented: they tell the reader exactly what to click, select, or do.
Every part of the interface should be documented, every built-in analysis
explained, and common workflows guided end-to-end. The writing is friendly
but never chatty — clear enough for a first-timer, useful enough for an
expert.

---

## Content principles

- **Show, don't just tell** — screenshots and short video clips (animations,
  screen recordings) are first-class content. Use them wherever they help the
  reader orient themselves or follow a sequence of steps.
- **Accessibility matters** — all images need descriptive alt text, videos
  should have captions or a written equivalent, and heading structure should
  be logical and consistent throughout.
- **Direct and instructional** — tell the reader exactly what to click,
  select, or type. No filler, no over-explaining.

---

## Sections

### 1. User Manual / UI Reference *(highest priority)*

The core reference for the jamovi interface. Covers every menu and tab
systematically: the file (hamburger) menu, the Variable, Data, Analyses,
Plots, and Edit tabs, the Module Library, and the Options (kebab) menu. The
goal is that a user can find any interface element here and know exactly what
it does and how to use it.

**Audience:** New users learning the interface; teachers transitioning from
other software; anyone who wants to know what a menu item does.

**Key content areas:**
- File (hamburger) menu — open, save, import, export, and related options
- Variable tab
- Data tab
- Analyses tab
- Plots tab
- Edit tab
- Module Library
- Options (kebab) menu

**Relationship to Getting Started:** The existing Getting Started section
(installation, first steps, running an analysis) should remain as a short
onboarding path for total beginners. The UI Reference is a separate, deeper
section that a user returns to when they want to know what a specific menu
item or tab does. The two coexist — Getting Started gets you up and running,
the UI Reference tells you everything.

**Current state:** The Getting Started section covers installation and first
steps, but there is no systematic UI reference. This is the largest gap in
the current docs.

---

### 2. Built-in Analyses

A reference section covering every analysis that ships with jamovi.
Each page should explain what the analysis does, how to set it up, and
what the output means — with screenshots showing the options panel and a
typical result.

**Audience:** Researchers and students running analyses.

**Key content areas:** Descriptives, t-tests, ANOVA, regression,
frequencies and chi-square, correlations, factor analysis (EFA/CFA),
reliability, and non-parametrics.

**Current state:** Descriptives, t-tests, ANOVA, regression, chi-square, correlations, factor analysis (EFA/CFA), are
partially covered. The section needs to be completed and made consistent.

---

### 3. Data Handling

Covers how to work with data in jamovi: variable types, computed and
transformed variables, filtering, restructuring, date handling, and common
data recipes.

**Audience:** Users preparing their data before analysis.

**Current state:** Already fairly comprehensive (10 pages). Can grow organically as new use cases surface.

---

### 4. How to...

End-to-end task guides for common workflows — the answer to "how do I
do X in jamovi?" Pages should be goal-oriented and walk the reader through
a complete task from start to finish.

**Audience:** Users who know what they want to accomplish and need
step-by-step guidance.

**Key content areas to add:** Importing and exporting data in various
formats, working with missing data, combining datasets, annotating and
sharing output. This section should grow based on the questions users
actually ask.

**Current state:** Very thin — only 3 pages. Significant room to grow.

---

### 5. Switching to jamovi

Helps users coming from another tool transfer what they already know.
Side-by-side comparisons show how a familiar workflow maps to jamovi.

**Audience:** Experienced users of SPSS, R, Excel, Stata, or SAS making
the switch.

**Key content areas:** At minimum, add R, Excel, and Stata to the existing
SPSS coverage.

**Current state:** SPSS-only (~20 pages). The section should be renamed
from "From SPSS to jamovi" to something more general like "Switching to
jamovi."

---

## Translations

The docs are translated into 25+ languages via Weblate. Translations are a
core part of the project, not an afterthought.

**What this means in practice:**
- Write with translation in mind — short, plain sentences; no idioms; consistent
  terminology throughout.
- All alt text and video captions need to be translatable too.
- Adding a new page is not just dropping an MDX file — it also needs to be
  wired into the Weblate translation pipeline. Familiarise yourself with this
  workflow before adding new sections.

---

## Out of scope

**Module documentation.** jamovi has a rich third-party module ecosystem, but
documenting individual modules is out of scope for this site. The Module
Library page (in the UI Reference) should explain how to find, install, and
manage modules — that is sufficient. Per-module documentation belongs with the
modules themselves, not here.

---

## Suggested additions

These are not required up front but are high-value additions worth planning
for.

### Keyboard shortcuts / Quick reference

A single page listing all keyboard and mouse shortcuts. Useful for power
users and for teachers running live demos. Low effort, high value.

### Reporting results

A guide on reporting jamovi output in academic writing — APA format examples
for common analyses, template language, and guidance on tables and figures.
Very useful for students and researchers writing up results.

---

## Priorities

1. **User Manual / UI Reference** — biggest gap, most broadly useful
2. **Built-in Analyses** — complete and make consistent what already exists
3. **Switching to jamovi** — expand beyond SPSS
4. How-tos, keyboard shortcuts, and reporting results can grow over time
