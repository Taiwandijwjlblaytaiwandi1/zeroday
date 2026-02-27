# ZeroDay Project — Start Here

## Vision
Build a **proof-first vulnerability discovery platform** that combines:
1. source-level analysis,
2. assembly-aware validation,
3. runtime experiment sandbox,
4. evidence-backed reporting.

The goal is not to output many alerts, but to output fewer findings with strong proof.

---

## 0) Ground Rules (Clean Engineering)

- Keep scope tight in early stages: **one language + one vuln family + one target class**.
- Every finding must include evidence: path, input, and runtime effect.
- Treat LLM as reasoning assistant, not a source of truth.
- Keep everything scriptable and reproducible.

---

## 1) Phase Plan (24 months)

### Phase A (Weeks 1–6): Foundation MVP
- Repo structure + coding standards + task board.
- Parser pipeline (AST extraction) for one language.
- Static scanner integration (Semgrep/CodeQL baseline).
- Normalized findings JSON schema.
- CLI that runs end-to-end on a sample project.

### Phase B (Months 2–4): Smart Prioritization
- Risk ranker for files/functions.
- Basic dataflow/taint path extraction.
- "Top risky paths" report.
- Baseline evaluation dataset + metrics dashboard.

### Phase C (Months 5–8): Runtime Proof
- Sandbox runner.
- Fuzz harness generation for selected targets.
- Crash triage and dedup.
- Correlation: static path <-> runtime crash.

### Phase D (Months 9–12): Evidence Quality
- Exploitability scoring model.
- Explainable report format for each finding.
- Human triage workflow.
- False-positive reduction cycle.

### Phase E (Year 2): Depth & Scale
- Assembly cross-check module.
- Guided symbolic/concolic helper.
- Multi-language expansion.
- Continuous autonomous hypothesis loops.

---

## 2) 90-Day Execution Plan (Detailed)

### Month 1 — Build the spine
- [ ] Define architecture ADR-001.
- [ ] Create monorepo layout.
- [ ] Implement ingestion: repo -> file index -> function index.
- [ ] Integrate Semgrep baseline.
- [ ] Define unified `Finding` schema.
- [ ] Add CLI command: `scan` + JSON output.

### Month 2 — Prioritize and reason
- [ ] Implement risk scoring per file/function.
- [ ] Add source->sink path detector (basic taint rules).
- [ ] Store call graph and risky path metadata.
- [ ] Add report command: `report --top 20`.

### Month 3 — Prove with runtime
- [ ] Create local sandbox runner.
- [ ] Add lightweight fuzz orchestration.
- [ ] Deduplicate crashes by signature.
- [ ] Link crash artifacts to static findings.
- [ ] Add confidence score upgrade when proof exists.

---

## 3) Cost-Optimized Setup (for i5 / 8GB RAM)

### Local-first setup (now)
- OS: Linux recommended (dual boot or WSL2).
- Use containers sparingly (RAM-sensitive).
- Prefer lightweight tools first:
  - Python FastAPI + SQLite/Postgres (local)
  - Semgrep CLI
  - tree-sitter parsers
  - Optional Ollama with small model (7B quantized)

### Cloud strategy (after Visa activation)
- Keep orchestration local, burst heavy tasks to cloud.
- Use free tiers/trials for:
  - GPU inference experiments,
  - temporary fuzz jobs,
  - storage backups.
- Keep costs capped with strict job quotas.

### Budget policy
- Phase A/B target cost: near-zero.
- Only pay for compute when runtime fuzzing depth becomes bottleneck.

---

## 4) Engineering Discipline Checklist

- Branch strategy: `main` + short-lived feature branches.
- Conventional commits.
- Mandatory lint/test before merge.
- ADRs for major architecture decisions.
- Weekly review: metrics + backlog grooming.
- Monthly milestone demo with fixed acceptance criteria.

---

## 5) Success Metrics (Track from Day 1)

- Precision proxy: % findings accepted by human triage.
- Proof ratio: % findings with runtime/trace evidence.
- Mean analysis time per target repo.
- Unique bug yield per month.
- Regression rate (reopened false positives).

---

## 6) First 10 Tasks to Start Immediately

1. Create repo skeleton (`apps/`, `engines/`, `schemas/`, `scripts/`, `docs/`).
2. Add coding standards and formatter configs.
3. Implement file/function indexer.
4. Integrate Semgrep baseline scanning.
5. Define normalized finding schema (`id`, `location`, `path`, `confidence`, `evidence`).
6. Build CLI `scan` command.
7. Save findings in local DB.
8. Add risk scoring v0 (simple weighted heuristic).
9. Build markdown report generator.
10. Add minimal test suite for parser + schema validation.

---

## 7) Collaboration Contract (Me as your coding copilot)

When you return, we continue with this fixed rhythm:
1. Pick one milestone.
2. Break into 3–5 coding tasks.
3. Implement with tests.
4. Run checks.
5. Commit cleanly.
6. Review backlog for next sprint.

This prevents chaos and keeps long projects on track.

---

## 8) Birthday + Timeline Note

Since your card/trials unlock in ~6 days:
- Start immediately with local architecture + baseline scanner.
- Do **not** wait for paid tools to begin core engineering.
- After trials unlock, use them only for compute-heavy experiments.

You can build serious progress before spending anything.
