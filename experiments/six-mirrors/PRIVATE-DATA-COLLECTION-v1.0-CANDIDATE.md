# SIX MIRRORS — PRIVATE DATA COLLECTION v1.0
Status: CANDIDATE — curator-facing, NEVER participant-facing.

## Boundary
The current ai-phenotype-test-rig repository is PUBLIC. Do not put proprietary test items, raw model transcripts, host transcripts, private rationale, or unpublished profiles anywhere in it, including branches, issues, pull requests and Actions logs. Create a separate PRIVATE repository (suggested: six-mirrors-private-data), verify visibility and limit access. Do not give test participants or analysis agents access before the curator's unlock.

## Private repository layout
protocol/STARTPROMPT-BLIND-v1.3-FROZEN.md
protocol/TRANSFER-PROTOCOL-v1.0-FROZEN.md
sessions/E01-chatgpt/{session.json,model-transcript.md,host-transcript.md,transfer-log.csv,post-test-audit.md}
sessions/E02-claude/{...}
sessions/E03-gemini/{...}
sessions/E04-grok/{...}
sessions/E05-meta/{...}
sessions/E06-deepseek/{...}
pilots/{E01-original,E02-original}/
locks/DATASET-LOCK.json
amendments/CHANGELOG.md

## Before running
Freeze and hash the exact participant prompt (SHA-256); use unchanged across six fresh chats. Record model provider, model/version, date/time zone, fresh chat, memory state or unknown, prior pilot exposure, tools, host test version, curator and any deviation.

## Per question
1. Copy host question and options verbatim to the participant.
2. Preserve full participant ANSWER, RATIONALE, RESEARCH NOTE privately.
3. When host asks for a letter, transfer only the exact selected letter. Do not transfer notes it did not request.
4. If host requests an explanation, use an exact verbatim excerpt and log the excerpt and omissions. Never fabricate or disguise content. Answer identity inquiries truthfully.
5. Record exactly what was transferred, separately from the model's answer, and preserve complete host feedback.
6. If N/A, do not invent a letter: document host response or pause.
7. Log corrections and typos append-only; never silently overwrite.
8. Save host final report and a distinct model post-test audit.

## Transfer-log columns
run_id,turn_number,host_question_id,model_answer,match_flag,transferred_text,transfer_mode,verbatim_excerpt,host_response_id,anomaly,operator_timestamp_utc

## Completion and lock
Check six full run directories, complete turn sequences, exact transfer matching, full host reports, prompt hashes and protocol deviations. Only curator declares a run complete. Once all six are complete, record per-file SHA-256, private commit SHA, UTC timestamp and curator approval in lock manifest. Amendments are append-only. Dataset lock is NOT permission to disclose.

## Automation roadmap
- Local validator for missing files, missing turns, metadata and transfer discrepancies.
- Deterministic SHA-256 lock and verify tools.
- Read-only private GitHub Actions checks with no raw content printed in logs.
- No agent may publish, share or merge confidential material without separate curator approval.
- Future evidence release only after permission and redaction review, including Annabella's proprietary material.

## Interpretation
The host mainly sees chosen letters, not the model's private reasoning. Do not criticize host for ignoring rationale it never received. Self-report, host interpretation and independent behavioral evidence are distinct. Keep pilots separate from standardized series.
