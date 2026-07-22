Repository assistant runtime (placeholder)

This directory is reserved for the eventual deckbuilding assistant code. Suggested layout:

- src/assistant/
  - ingest/   # code that reads/parses knowledgebase markdown
  - api/      # small internal API that exposes knowledgebase queries
  - models/   # model wrappers, prompts, and utilities
  - cli.py    # optional CLI entrypoint for local testing

Do not add assistant runtime until the knowledgebase ingestion API is stable. When adding code here, update CLAUDE.md and .github/copilot-instructions.md with any runtime or architecture changes.
