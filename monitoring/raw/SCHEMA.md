# Raw Monitoring Record Schema

This document defines the minimum structure for incoming AI milestone monitoring records.

## Required fields

- model
- observed_at
- event
- source
- source_url
- timing_precision
- monitoring_record_id

## Models

- ChatGPT
- Claude
- Gemini

## Timing precision

Allowed values:

- second
- minute
- date
- unknown

No clock time may be invented when the source does not provide one.

## Verification

Raw monitoring records are observations only.

They are not automatically verified milestones.

Verification must occur before promotion to the AI Rectification Lab MILESTONE INBOX and MASTER MILESTONES.

## Example structure

```yaml
monitoring_record_id: MON-YYYYMMDD-XXXX
model: ChatGPT
observed_at: YYYY-MM-DD
event: "Description of observed event"
source: "Source name"
source_url: "https://example.org/source"
timing_precision: date
verification_status: pending

## Integrity rule

Raw monitoring records are immutable after ingestion.

The original observation must be preserved exactly as received.

No later process may:

- overwrite the original raw record
- alter its timestamp
- alter its source
- alter the wording of the observed event
- add information to the original observation and present it as source data
- modify the record to improve agreement with a rectification hypothesis

Any correction, verification, interpretation, extraction, or enrichment must be stored as a separate record or in a separate processing layer.

The raw record is the audit source.

A record may only be promoted from raw monitoring to the AI Rectification Lab after verification. Promotion does not alter or delete the original raw record.

Historical records must remain recoverable through Git history.
