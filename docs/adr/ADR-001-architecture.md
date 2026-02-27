# ADR-001: Initial architecture (MVP)

## Status
Accepted

## Context
The project currently has no executable code and needs a minimal, testable baseline for Phase A.

## Decision
Adopt a lightweight Python architecture with these modules:
- `indexer`: file discovery + function extraction
- `risk`: deterministic heuristic risk scoring
- `scanner`: orchestration + optional Semgrep integration
- `cli`: `zeroday scan <target>` entrypoint

## Consequences
- Fast local startup on low-resource hardware.
- Easy extension path toward taint analysis and runtime evidence modules.
- Semgrep remains optional so scans still work without external dependencies.
