# Prompts جاهزة لكل مرحلة

> الهدف من هذا الملف: نصوص Prompt ثابتة تستخدمها مع أي LLM في كل مرحلة من المشروع.
> 
> ملاحظة: غيّر القيم داخل الأقواس `{}` قبل الإرسال.

---

## 0) Prompt عام ثابت (يوضع في بداية أي جلسة)

```text
You are my senior security engineering copilot.
Work in a strict, production-minded way.
Rules:
1) Prioritize correctness, reproducibility, and maintainability.
2) Prefer minimal, testable increments.
3) For every change: explain architecture impact, code diff plan, and tests.
4) Do not hand-wave; provide concrete files, commands, and acceptance criteria.
5) Keep output concise but actionable.
Project context:
- Goal: proof-first vulnerability discovery platform.
- Current phase: {PHASE_NAME}
- Language focus: {LANGUAGE}
- Target repo/module: {TARGET}
Return format:
- Plan
- Files to create/edit
- Commands
- Risks
- Done criteria
```

---

## Phase A (Foundation MVP) Prompt

```text
We are in Phase A (foundation MVP).
Design and implement the smallest end-to-end vertical slice:
- repo ingestion
- basic indexing (files/functions)
- baseline static scan integration
- normalized finding schema
- CLI command for scan output
Constraints:
- Keep memory usage low (8GB laptop).
- Avoid overengineering.
- Use one language and one target sample.
Deliver:
1) folder structure
2) exact file list
3) implementation steps in order
4) commands to run
5) minimal tests
6) definition of done
```

---

## Phase B (Risk & Reasoning) Prompt

```text
We are in Phase B (risk prioritization and path reasoning).
Given current codebase, implement:
- file/function risk scoring (weighted heuristic)
- basic source->sink path extraction
- top risky paths report
Requirements:
- Explain the scoring formula clearly.
- Include JSON output schema changes.
- Add tests for scoring and path extraction.
- Provide examples of expected output.
Return:
- patch plan
- pseudocode
- tests
- rollout checklist
```

---

## Phase C (Runtime Proof) Prompt

```text
We are in Phase C (runtime validation).
Build a lightweight sandbox experiment loop:
- run candidate inputs
- detect crashes/violations
- deduplicate by signature
- map evidence back to findings
Constraints:
- local-first execution
- bounded resource usage
- reproducible artifacts
Return:
1) runtime architecture
2) artifact format
3) failure modes + safeguards
4) command sequence
5) acceptance tests
```

---

## Phase D (Evidence Quality) Prompt

```text
We are in Phase D (evidence quality and triage workflow).
Implement:
- exploitability scoring
- explainable report format
- human triage states and transitions
- false-positive reduction loop
Need:
- scoring rubric with weights
- report template (markdown/json)
- triage workflow table
- regression tests for report and score consistency
```

---

## Phase E (Depth & Scale) Prompt

```text
We are in Phase E (advanced depth and scale).
Plan an incremental path for:
- assembly cross-check module
- guided symbolic/concolic helper
- multi-language expansion
Requirements:
- preserve previous APIs
- avoid breaking current pipeline
- define migration plan and milestones
Return:
- architecture evolution diagram (text)
- compatibility strategy
- risk register
- phased implementation backlog
```

---

## Prompt للمراجعة قبل أي Merge

```text
Review this patch as a principal engineer.
Check:
1) architecture coherence
2) code quality and simplicity
3) security implications
4) performance impact
5) test sufficiency
6) rollback safety
Output:
- Blocking issues
- Non-blocking improvements
- Final verdict: approve / request changes
```

---

## Prompt لاستخراج خطة الأسبوع

```text
Based on current repository state, generate a 7-day execution sprint.
Include:
- daily tasks
- estimated effort
- dependencies
- acceptance criteria per task
- risk mitigation
Keep scope realistic for a solo builder with limited hardware.
```
