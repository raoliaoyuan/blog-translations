# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a content repository for Chinese translations of English technical articles (deep technical analysis, architecture breakdowns, engineering practice pieces). It is not a code project — there is no build, lint, or test tooling. Each translated article lives in its own subdirectory alongside its referenced images and any source feeds (e.g. `feed.xml`).

## Translation standard (authoritative)

All translation work in this repository must follow [SKILLS_技术文章翻译规范.md](SKILLS_技术文章翻译规范.md). Key rules that are easy to violate and worth internalizing before editing:

- **Terminology on first use**: professional technical terms must be annotated as `中文翻译（English Original）` the first time they appear. After first use, either Chinese or English alone is fine; re-annotate only if the term reappears after ~3+ large sections.
- **Do not translate**: code identifiers, commands, paths, product/project names (Claude Code, npm, Bun, GrowthBook, etc.), industry-standard abbreviations (API, CLI, token, schema, harness, A/B), and established English phrases used as-is in the industry (vibe coding). `token` and `bug` stay as-is.
- **Tone is restrained**: no exclamation marks, no internet slang ("牛逼"/"炸裂"/"干货"), no synonym-stacking emphasis, no translator commentary in the body. Translator notes only as `（译注：...）` and only when omitting would lose information.
- **Structure is preserved**: headings, `---` thematic breaks, lists, bold/italic, and image paths match the original exactly. Long English sentences should be split into natural Chinese sentences rather than rendered as translation-ese.
- **Front matter**: every translated article begins with an author / date / original-link block in the format shown in the spec §3.2.
- **Before delivering**: run through the self-check list in §6 of the spec (terminology annotations, no added emphasis, identifiers untranslated, structure parity, links preserved, front matter complete).

When the user asks for a translation, default to following this spec without re-asking. If a passage is ambiguous in the source, preserve the ambiguity rather than resolving it with invented content.

## Working with article directories

Each article directory typically contains:
- The translated Markdown file (Chinese filename or transliterated English).
- Images referenced from the Markdown, with paths kept relative and unchanged from the original layout.
- Optionally a `feed.xml` or similar source artifact captured alongside the translation.

When editing an existing translation, match the conventions already present in that file (term choices, section ordering) rather than re-deriving them from the spec.

## Context discipline (read this before every task)

Each article directory is fully self-contained and independent. To avoid polluting the context window with unrelated content:

- **Read only the target article's files.** Never read files from sibling article directories unless the user explicitly asks for a cross-article comparison.
- **Do not glob the entire repo.** When locating a file, scope the search to the specific subdirectory the user named, not `/Users/roger/Work/Blog/**`.
- **Do not read `feed.xml` or source artifacts** unless the task explicitly requires the original source text.
- **Do not read images** (`.png`, `.jpg`, `.gif`, `.svg`, `.webp`). They are referenced assets, not content to process.
- **Read the translation spec only when starting a new translation or when a rule is unclear.** Do not re-read it for every edit to an existing file.
- **Minimal file set per task**: identify the single file (or smallest set) needed to complete the task, read only that, and proceed. Ask the user if the target file is ambiguous rather than reading multiple candidates.
