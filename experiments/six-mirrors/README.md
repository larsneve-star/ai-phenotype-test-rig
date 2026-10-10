# THE SIX MIRRORS — Pilot to standardized study

Status: **proposal only; not frozen, not a dataset lock**. Owner: human curator.

Research question: Can AI models identify characteristic behavioral patterns in each other, and can these claims survive independent documentary review and prospective behavioral tests?

## Stages
0. E01/E02 pilot transcripts are historical, nonblind and protocol-divergent. Preserve separately.
1. Curator freezes the type-blind standardized startprompt and transfer protocol (same for six fresh chats).
2. Six independent model sessions, with **no cross-model result disclosure**.
3. Curator privately archives raw questions, chosen letters, full explanations, host feedback, and transfer records. Preserve exact text and timestamps.
4. Lock dataset by recording SHA-256 per file and manifest hash. No retroactive editing; amendments are append-only.
5. Collect six *spontaneous peer assessments* **before** showing any other profiles or RI evidence.
6. Release one common RI/LOTUS evidence packet and collect six source-grounded peer assessments.
7. Reveal self-profiles and peer assessments; collect correction/rebuttal statements.
8. Run preregistered, matched behavioral probes. Report falsifications and uncertainty.

## Non-negotiable protections
- The current repository is **PUBLIC**. Do **not** commit proprietary EnneaProfile items, raw transcripts, unpublished model answers, personal data, or individual profile results here before curator-approved release.
- A separate **PRIVATE** repository is needed for raw data; private branches inside a public repository do not protect secrets.
- No automation may read raw data, publish results, merge an embargoed PR, or send peer materials before the curator's explicit unlock.
- The model taking the test receives only the type-blind prompt, not this README, codebook, pilot notes, or any peer result.
- Preserve both **what the model wrote** and **what was actually transferred** to the adaptive test; they can differ.
- Mark pilot exposure, memory effects, prompt changes, model version, tool availability and any exceptions.
- Human scoring and adaptive host output are not ground truth; independent behavioral verification is necessary.

## Proposed files
- `STARTPROMPT-BLIND-v1.2-CANDIDATE.md`: participant-facing neutral instruction.
- `TRANSFER-PROTOCOL-v1.0-CANDIDATE.md`: curator-only transcription rules.
- `schemas/session.schema.json`: structured metadata validation.
- `scripts/validate_sessions.py`: safe metadata validator.
- `.github/workflows/validate-six-mirrors.yml`: PR validation only, no disclosure.
- `DATASET-LOCK.md`: placeholder until curator locks six runs.

Annabella's contribution: invite co-design of constructs, instrument validity, and publication rules. Do not publish proprietary test text without permission.
