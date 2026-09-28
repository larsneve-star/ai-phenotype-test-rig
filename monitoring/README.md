# Monitoring

This directory is the interface between the live AI milestone monitoring stream and the AI Phenotype Test Rig.

## Purpose

Raw monitoring observations are preserved here before any event is considered for promotion into the AI Rectification Lab.

## Models

The monitoring stream currently covers:

- ChatGPT
- Claude
- Gemini

## Data flow

Live monitoring → raw monitoring archive → extraction → verification → AI Rectification Lab MILESTONE INBOX

## Integrity

Raw monitoring records must not be silently overwritten.

Verified milestones are promoted separately into the AI Rectification Lab. Historical records and previous rectification snapshots remain unchanged.
