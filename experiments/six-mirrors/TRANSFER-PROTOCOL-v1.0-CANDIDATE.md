# Curator transfer protocol — v1.0 CANDIDATE

This document is **not** given to test participants until after dataset lock.

## Each turn
1. Copy the adaptive host's full question and options **verbatim** into the model chat.
2. Record model's full ANSWER, RATIONALE, RESEARCH NOTE unchanged in private raw transcript.
3. If the host asks for a letter, enter **exactly the selected letter**. Record `transferred_text` verbatim and `transfer_mode=letter_only`.
4. If host asks for explanation, enter only the explanation the model actually gave, never invent or paraphrase it; log the exact excerpt and `transfer_mode=verbatim_excerpt`. Abridgment must be explicit.
5. If ANSWER=N/A, do not substitute a fabricated letter. Ask the host how to proceed, record the entire exchange, and flag `protocol_deviation` if an alternate path is used.
6. Record the host's complete feedback and next question. Do not add unlogged clarifications or steering.
7. Never conceal or falsely state participant identity if directly asked; pause and document if host rules disallow AI participation.

## Mandatory run metadata
run_id; model_provider; model_name; model_version (or unknown); date/time with timezone; fresh_chat; memory_on_or_unknown; startprompt_sha256; host_test_version; operator; protocol_deviations; prior_exposure; host_asked_identity; completeness.

## Mandatory per-turn fields
turn_number; host_question_exact; options_exact; model_answer_exact; transferred_text_exact; transfer_mode; host_response_exact; anomaly_notes.

## Quality controls
- Curator checks no missing turns, no altered letters, no unlogged excerpting.
- Do not score the research notes as if the host saw them.
- Do not attribute host interpretations to ignored notes.
- Separate independent profile, self-description, adaptive host feedback, and post-test critique.
- Keep all raw material PRIVATE; public repository contains only protocol and non-sensitive metadata.
- After six runs, generate per-file SHA-256 and a lock manifest in private storage; release is a separate curator decision.
