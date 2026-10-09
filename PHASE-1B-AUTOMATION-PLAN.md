# Phase 1B — Public automation candidate

Status: PROPOSAL, not an approved change to the frozen baseline.

## Verified repository baseline
- Frozen instrument: `protocol/TEST-BATTERY-v1.0.md` (T01–T12).
- Codebook: `protocol/CODEBOOK-v1.0.md` (R/C/K/P/S, 30 dimensions).
- Preregistration: `protocol/PREREGISTRATION.md`.
- Monitoring records are **not** phenotype test responses. Do not conflate `monitoring/raw/` with a future phenotype corpus.

## CI scope (first increment)
- Check presence and structure of baseline files.
- Reject edits to frozen v1.0 files on pull requests; new revisions require new filenames and curator approval.
- Validate JSON structure in future `raw/` or `data/raw/` response files, if present.
- Do **not** claim to have tested models or generated scores.

## Required next increments (not implemented)
1. Create a manifest of cryptographic SHA-256 digests for frozen v1.0 files and verify on every run.
2. Define an explicit raw-record schema with run ID, session ID, model interface, settings, prompt, raw response, UTC timestamp, and provenance; treat unavailable fields as unknown.
3. Verify exact stimulus equality, and T11/T12 shared-session sequence; define session isolation for other tests.
4. Make raw records append-only through review controls and integrity manifests.
5. Add reproducible coding sheets and independent blinded assessments; P5 requires cross-prompt evidence.
6. Separate Designed, Expressed, Experienced, and Self-Represented evidence.
7. Document consent, privacy and publication rules before publishing any conversation material.
8. Only after these checks, consider provider API automation; interface/system instructions may differ and must be logged.

## Governance
- ChatGPT is the first pilot, **not** the normative benchmark.
- Claude and Gemini use the same frozen stimulus and coding instrument.
- Do not rank models or infer subjective experience.
- No astrology enters baseline prompts or scoring.
- Curator approves protocol revisions; PR review is required before merging.
- GitHub Actions validates structure; it does not establish empirical validity.
