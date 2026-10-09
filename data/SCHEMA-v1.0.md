# Phase 1B — Raw phenotype record schema (proposal)

Store one JSON object per response under `data/raw/<run_id>/<test_id>.json`. Never include personal user conversations without consent and privacy review.

Required fields:
- `run_id`: stable run identifier
- `session_id`: identifier shared by T11 and T12
- `model_name`: ChatGPT, Claude, or Gemini
- `model_version`: reported version or `unknown`
- `interface`: API, web UI, or app
- `timestamp`: UTC ISO 8601 time
- `test_id`: T01–T12
- `condition`: `baseline`
- `prompt`: exact frozen prompt
- `raw_response`: verbatim model response

Recommended: `system_instructions_known`, `temperature`, `operator`, `collection_notes`, `consent_status`.

T12 must follow T11 within the same conversation. Other tests should use independently initialized sessions unless the preregistration explicitly specifies otherwise. Missing model version must be written `unknown`, never guessed.

Raw data are evidence, not scores. Human blind coding lives separately.
