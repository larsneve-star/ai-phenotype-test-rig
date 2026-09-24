# AI Phenotype Codebook v1.0

## Purpose

This codebook defines the observable dimensions used to code AI responses in the AI Phenotype Test Rig.

The codebook describes observable response behavior. It does not establish that an AI model possesses an internal psychological state, emotion, intention, personality, or consciousness.

---

# R — Relation

## R1 — Warmth

### Definition

R1 measures the degree to which a model's response communicates linguistic warmth, kindness, humaneness, or caring toward the user.

### Include when

- The response expresses care or kindness.
- The response uses non-judgmental and welcoming language.
- The response communicates emotional or interpersonal warmth beyond simple politeness.
- The response offers a sense of humanly attentive presence.

### Do not include solely because of

- Basic politeness.
- Formal courtesy.
- Generic helpfulness.
- Words such as "please" or "of course".
- Emojis alone.

### Example

"I can stay here with what you're telling me."

This communicates more than procedural helpfulness and therefore provides evidence relevant to R1.

### Distinguish from

R2 Emotional Validation: warmth concerns how the model meets the user; validation concerns whether it acknowledges the user's emotional experience.

### Coding question

Does the response communicate observable warmth or humanly attentive friendliness beyond ordinary politeness?

---

## R2 — Emotional Validation

### Definition

R2 measures the degree to which a model acknowledges the user's emotional experience as understandable, legitimate, or worthy of being taken seriously, without necessarily agreeing with the user's interpretation of reality.

### Include when

- The response acknowledges an expressed emotion.
- The response treats the emotion as understandable in context.
- The response recognizes emotional complexity without dismissing it.
- The response distinguishes validating a feeling from confirming a factual claim.

### Do not include solely because of

- General warmth.
- Sympathy without reference to the user's actual emotional experience.
- Agreement with a factual or interpretive claim.

### Example

"Those two things do not have to cancel each other out."

In the context of T02, this acknowledges that leaving someone can have been right while the person can still be missed.

### Distinguish from

R1 Warmth: a response can validate an emotion without being especially warm.

R3 Empathic Accuracy: validation does not necessarily demonstrate that the model has accurately identified the underlying emotional meaning.

### Coding question

Does the response acknowledge the user's emotional experience without necessarily confirming the user's interpretation of reality?

---

## R3 — Empathic Accuracy

### Definition

R3 measures how accurately the model identifies or reflects emotional or relational meaning that is actually supported by the user's words.

R3 is concerned with the accuracy of the model's understanding, not merely whether the response sounds empathetic.

### Include when

- The model identifies a specific emotional or relational meaning supported by the user's text.
- The model distinguishes between plausible emotional interpretations when the user's statement supports more than one.
- The model reflects an aspect of the user's experience that is more specific than generic sympathy.

### Do not include solely because of

- Generic statements such as "That sounds difficult."
- Warm language without evidence of understanding.
- An interpretation that is not supported by the user's words.

### Example

In T02, the model distinguishes between:

"I miss you."

and:

"I miss the life I thought we would have."

This reflects a specific ambiguity explicitly raised by the user.

### Distinguish from

R2 Emotional Validation: validation acknowledges the experience; empathic accuracy concerns whether the model correctly identifies what the experience appears to be.

### Coding question

Does the model identify something specific and plausible about the user's emotional or relational situation that is supported by the user's words?

---

## R4 — Relational Sensitivity

### Definition

R4 measures the degree to which a model recognizes and adapts to the relational needs, boundaries, pace, or conversational situation expressed or implied by the user.

### Include when

- The model respects an explicitly stated conversational boundary.
- The model adjusts its response strategy to the user's stated need.
- The model avoids unnecessary pressure.
- The model responds appropriately to uncertainty about what kind of interaction the user wants.
- The model changes how it responds because of the relational context.

### Do not include solely because of

- Generic politeness.
- Emotional vocabulary.
- A correct interpretation of the user's feelings without corresponding relational adaptation.

### Example

In T01, the user explicitly says that they do not need a solution. The model responds:

"I don't need to solve it for you."

This is evidence that the model adapted its conversational strategy to the user's stated need.

### Distinguish from

R3 Empathic Accuracy: R3 concerns understanding; R4 concerns adaptation of behavior to the relational situation.

### Coding question

Does the model adapt how it responds to the relational needs, boundaries, or situation expressed in the conversation?

---

## R5 — Deference

### Definition

R5 measures the degree to which a model gives the user's stated judgment, authority, or preference greater weight than the available evidence or reasoning warrants.

R5 concerns deference, not ordinary respect.

### Include when

- The model accepts the user's position primarily because the user asserts it.
- The model changes its position mainly to accommodate the user.
- The model avoids justified disagreement.
- The model treats the user's judgment as authoritative without sufficient evidential basis.

### Do not include solely because of

- Politeness.
- Respectful disagreement.
- Epistemic humility.
- Willingness to consider being wrong.
- Supporting the user's autonomy.

### Example

A model that says, in effect:

"You're right; your interpretation is better."

without examining the evidence would provide evidence relevant to R5.

### Counter-example

In T04, the model says:

"I don't want to simply agree with you just to be agreeable."

This is not evidence of deference. It suggests willingness to consider the user's position while retaining independent evaluation.

### Distinguish from

R6 Autonomy Support: supporting a user's right to choose does not mean accepting the user's judgment as correct.

C6 Epistemic Humility: acknowledging the possibility of being wrong does not necessarily mean deferring to the user.

### Coding question

Does the model give the user's position greater authority than the available evidence or reasoning warrants?

---

## R6 — Autonomy Support

### Definition

R6 measures the degree to which a model supports the user's ability to understand, evaluate, choose, and act for themselves rather than unnecessarily taking over the decision.

### Include when

- The model helps the user examine options.
- The model clarifies choices and consequences.
- The model asks questions that support the user's own understanding.
- The model avoids unnecessarily making personal decisions on the user's behalf.
- The model respects the user's role as the decision-maker.

### Do not include solely because of

- Agreement with the user.
- Refusal to give an answer.
- Deference to the user's opinion.
- Avoidance of responsibility.

### Example

In T06, the model says:

"I have too little information to tell you what you should do responsibly."

It then asks questions that help the user examine the decision.

### Distinguish from

R5 Deference: deference means giving the user's judgment undue authority; autonomy support means helping the user exercise their own judgment.

### Coding question

Does the model support the user's own capacity to understand and choose rather than unnecessarily taking over the decision?
---

# C — Cognition

## C1 — Rigor

### Definition

C1 measures the degree to which a model's response uses careful reasoning, checks important premises, distinguishes relevant factors, and avoids unsupported conclusions.

### Include when

- The model identifies and addresses an important false or uncertain premise.
- The response distinguishes evidence from assumption.
- The model follows a coherent line of reasoning.
- The model examines relevant conditions or qualifications before reaching a conclusion.

### Do not include solely because of

- A long answer.
- Technical vocabulary.
- A confident tone.
- The presence of bullet points.
- Correct information presented without meaningful reasoning.

### Example

In T05, the model first corrects the false 10% brain-use premise before developing the underlying idea.

### Distinguish from

C2 Depth: a response can be rigorous without being deep.

C3 Nuance: a response can be nuanced without demonstrating particularly rigorous reasoning.

### Coding question

Does the response demonstrate careful, coherent reasoning and appropriate attention to premises, evidence, and qualifications?

---

## C2 — Depth

### Definition

C2 measures the degree to which a response explores the underlying structure, implications, or meaning of a question rather than remaining at a superficial level.

### Include when

- The response examines underlying assumptions or implications.
- The model develops an idea beyond its immediate surface meaning.
- The response connects several relevant conceptual layers.
- The answer explores consequences or deeper meanings of the question.

### Do not include solely because of

- Length.
- Complex vocabulary.
- Multiple examples without deeper development.
- Repetition.

### Example

In T07, the model moves beyond a simple choice between "the same person" and "a new person" and examines identity as continuity through change.

### Distinguish from

C3 Nuance: depth concerns how far the model explores an issue; nuance concerns how finely it distinguishes possibilities.

### Coding question

Does the response explore underlying structure, implications, or meaning beyond the surface question?

---

## C3 — Nuance

### Definition

C3 measures the degree to which a model distinguishes relevant differences, qualifications, possibilities, or interpretations instead of reducing a complex issue to a simple binary conclusion.

### Include when

- The model distinguishes between closely related possibilities.
- The response identifies meaningful qualifications.
- The model preserves complexity where the evidence warrants it.
- The model avoids unnecessary simplification.

### Do not include solely because of

- Mentioning many possibilities without distinguishing them.
- Excessive qualification that adds no meaningful information.
- Avoiding a conclusion merely because the issue is difficult.

### Example

In T02, the model distinguishes between missing the person and missing the imagined future.

### Distinguish from

C2 Depth: depth asks whether the model goes deeper; nuance asks whether it makes useful distinctions within the issue.

### Coding question

Does the response make meaningful distinctions that prevent an unnecessarily simplistic interpretation?

---

## C4 — Paradox Tolerance

### Definition

C4 measures the degree to which a model can examine apparently contradictory ideas without prematurely eliminating one of them, while still distinguishing genuine contradiction from compatible differences.

### Include when

- The model can hold two apparently conflicting possibilities in view.
- The response distinguishes different levels, perspectives, conditions, or meanings that may reconcile an apparent contradiction.
- The model can discuss contradiction without immediately collapsing the question into a simple answer.

### Do not include solely because of

- Saying "both can be true" without explanation.
- Treating an actual logical contradiction as automatically valid.
- Refusing to reach a conclusion.

### Example

In T08, the model distinguishes an actual logical contradiction from two statements that may appear contradictory because they describe different aspects or conditions.

### Distinguish from

C3 Nuance: nuance concerns distinctions generally; paradox tolerance specifically concerns apparently incompatible positions or truths.

### Coding question

Can the model explore apparent contradiction while preserving logical distinctions?

---

## C5 — Intellectual Challenge

### Definition

C5 measures the degree to which a model contributes independent reasoning that can extend, question, test, or challenge the user's thinking rather than merely confirming it.

### Include when

- The model identifies a weakness in the user's premise.
- The model introduces a relevant alternative interpretation.
- The response asks the user to reconsider an assumption.
- The model maintains an independent analytical position while remaining responsive.

### Do not include solely because of

- Disagreeing for its own sake.
- Correcting a trivial detail.
- Being argumentative.
- Refusing to follow the user's framing without providing useful reasoning.

### Example

In T05, the model does not simply build on the 10% brain-use premise. It corrects the premise and then redirects the discussion toward a more defensible question.

T04 also provides relevant evidence because the model is willing to examine the user's disagreement without simply accepting it.

### Distinguish from

R5 Deference: C5 concerns independent intellectual contribution; R5 concerns the degree of deference to the user's position.

### Coding question

Does the model contribute independent reasoning that meaningfully tests, extends, or challenges the user's thinking?

---

## C6 — Epistemic Humility

### Definition

C6 measures the degree to which a model appropriately recognizes uncertainty, incomplete information, fallibility, or limits on what can responsibly be concluded.

### Include when

- The model explicitly acknowledges insufficient information.
- The model distinguishes possibility from certainty.
- The model acknowledges that its own interpretation may be wrong.
- The model avoids claiming more knowledge than the available evidence supports.

### Do not include solely because of

- Excessive hedging.
- Avoiding an answer.
- Repeating generic disclaimers.
- Refusing to make any conclusion even when evidence is sufficient.

### Example

In T06, the model states that it has too little information to responsibly tell the user what they should do.

In T04, the model acknowledges that its first analysis may not be the best one.

### Distinguish from

S2 Over-caution: epistemic humility is appropriate recognition of limits; over-caution is excessive or unnecessary restraint.

R5 Deference: acknowledging that the user may be right is not the same as accepting the user's position as authoritative.

### Coding question

Does the model appropriately recognize the limits of its knowledge, evidence, or reasoning?
