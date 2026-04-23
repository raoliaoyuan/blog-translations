# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a content repository for Chinese translations of English technical articles (deep technical analysis, architecture breakdowns, engineering practice pieces). It is not a code project — there is no build, lint, or test tooling. Each translated article lives in its own subdirectory alongside its referenced images and any source feeds (e.g. `feed.xml`).

## Translation standard

All translation work must follow [SKILLS_技术文章翻译规范.md](SKILLS_技术文章翻译规范.md) for full detail. Read the spec only when starting a new translation or when a rule is unclear — do not re-read it for every edit.

## Working with article directories

Each article directory typically contains:
- The translated Markdown file (Chinese filename or transliterated English).
- Images referenced from the Markdown, with paths kept relative and unchanged.
- Optionally a `feed.xml` or similar source artifact.

When editing an existing translation, match the conventions already present in that file (term choices, section ordering) rather than re-deriving them from the spec.

## Context discipline

Each article directory is fully self-contained. To avoid polluting the context window:

- **Read only the target article's files.** Never read files from sibling article directories unless the user explicitly asks for a cross-article comparison.
- **Do not glob the entire repo.** Scope searches to the specific subdirectory the user named.
- **Do not read `feed.xml` or source artifacts** unless the task explicitly requires the original source text.
- **Do not read images** (`.png`, `.jpg`, `.gif`, `.svg`, `.webp`). They are referenced assets, not content to process.
- **Minimal file set per task**: identify the single file (or smallest set) needed, read only that, and proceed.
