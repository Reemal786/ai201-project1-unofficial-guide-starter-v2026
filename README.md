# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

The Unofficial Guide is a retrieval-augmented  system built using the `city_guides` corpus, which contains 14 travel guides. The system retrieves relevant sections from these guides and uses them to answer questions such as how to travel between locations, when to visit, and what activities are available.

## Chunking Strategy

**Chunk size:** One labeled section of a city guide per chunk, using the `##` as natural boundaries. If a section is long, it will be divided at paragraph boundaries rather than in the middle of a sentence.
**Overlap:** 0 characters between sections

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `guide_accessibility.md#0` — produced by: `chunker.py::split_documents`

```
# Getting around the region with limited mobility An honest assessment rather than a promotional one. Some of these places are difficult and it is better to know in advance.

```

**Chunk 2** — source: `guide_corry_vale.md#6` — produced by: chunker.py::split_documents`

```
## When to go May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.
```

**Chunk 3** — source: `guide_givens_mill.md#3` — produced by: `chunker.py::split_documents`

```
## Eat and drink A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.

```

**Chunk 4** — source: `guide_kestrelford.md#6` — produced by: `chunker.py::split_documents`

```
## When to go Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.
```

**Chunk 5** — source: `guide_regional_transport.md#1` — produced by: `chunker.py::split_documents`

```
## The railway The line runs along the river valley, connecting Brightwater to the regional hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line north of Brightwater closed in 1963 and everything beyond it is bus or car. Tickets are cheaper booked the day before than on the day, and considerably cheaper than that booked a week ahead. There is no ticket office at Brightwater station outside weekday mornings; the machine on the platform takes cards only. For each one, ask: could someone answer a question using only this, without reading what came before or after?
```

## Sample Answer

**Question:** How many buses per day run from Brightwater to Givens Mill on weekdays?

**Answer:**

```text
Four buses a day run from Brightwater to Givens Mill on weekdays (from guide_givens_mill.md).
```

**Source:** `guide_givens_mill.md`
```

**My relevance cutoff:** 0.6

I kept the relevance cutoff at 0.6 after comparing the best retrieval
distances for my five in-corpus questions with five out-of-scope questions.
The in-corpus questions ranged from 0.249 to 0.390, while the out-of-scope
questions ranged from 0.754 to 0.899. Found the middle ground that feel between the two groups


| Question | In corpus? | Best distance |
|---|---|---|
| How many buses per day run from Brightwater to Givens Mill on weekdays? | Yes | 0.348 |
| What are the recommended months to visit Halden Bay while avoiding the busiest summer period? | Yes | 0.249 |
| How often do Marchwood trams run on weekdays? | Yes | 0.384 |
| What happens to Halden Bay during winter? | Yes | 0.390 |
| How long does it take to walk from Givens Mill to Brightwater along the river? | Yes | 0.261 |
| What is the capital of Mongolia? | No | 0.754 |
| How do I change the oil in a diesel engine? | No | 0.892 |
| Who won the 1994 World Cup? | No | 0.899 |
| What is the recommended dosage of ibuprofen? | No | 0.815 |
| How do I write a for loop in Rust? | No | 0.813 |

## How I Used AI

## How I Used AI

**1.** I used ChatGPT as a secondary resource while developing my chunking strategy. After inspecting the starter's fixed 800-character chunks and noticing that they cut through sentences and words, I decided that the Markdown structure of the city guides could provide better chunk boundaries. I discussed this approach with ChatGPT and used its feedback while implementing `split_documents()`. I then re-indexed the corpus and manually inspected the resulting chunks to evaluate whether they represented complete thoughts.

**2.** I used ChatGPT to check my interpretation of the retrieval results after testing five in-corpus and five out-of-scope questions. I compared the retrieval distances and found a clear separation between the two groups, with in-corpus distances ranging from 0.249 to 0.390 and out-of-scope distances ranging from 0.754 to 0.899. Based on my results, I chose to keep the existing 0.6 relevance cutoff and tested the gate to confirm that it rejected out-of-scope questions.

**3.** During Unit 2, I ran the before evaluation, manually reviewed the results against my five criteria, and found that all five met their targets. While reviewing the chunk samples, I noticed that one chunk contained only the heading `# When to visit the region`. I used ChatGPT to discuss why my chunking logic produced this result and to help trace it to how `split_documents()` handled content before the first `##` heading.

**4.** I decided to address the heading-only chunk as my Unit 2 improvement and used ChatGPT for feedback while updating the chunking logic to ignore sections without body text. I re-indexed the corpus, inspected three new sets of chunk samples, and ran the full evaluation again. I compared the before and after results and found that Criterion 4 improved to 5/5 across all three samples while the other four criteria continued to meet their targets.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks contain a complete section or thought | 4 of 5 | 4/5 | 5/5 | 5/5 | MET |
| 5. Answer contains the expected fact | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### Evidence — Before

**Criterion 1 — Retrieved chunks contain the answer**

Produced by `run_eval.py::main`, using retrieval from `store.py::search`.

For all 5 test questions, the retrieved sources contained the information needed to answer the question. Example from Run 1:

```text
Question: How many buses per day run from Brightwater to Givens Mill on weekdays?
Best distance: 0.3480 (passed the gate)
Sources retrieved: guide_givens_mill.md, guide_kestrelford.md, guide_marchwood.md, guide_regional_transport.md

Four buses a day run from Brightwater to Givens Mill on weekdays (from guide_givens_mill.md).
```

**Criterion 2 — Every answer names a source**

Produced by `run_eval.py::main` and `generate.py`.

All 15 generated answers named at least one source document. Example:

```text
What happens to Halden Bay during winter?

Halden Bay largely closes during the winter.

Source: guide_seasons.md
```

**Criterion 3 — Gate stops out-of-corpus questions**

Produced by `run_eval.py::check_out_of_scope`.

```text
refused  (best distance 0.754)  What is the capital of Mongolia?
refused  (best distance 0.892)  How do I change the oil in a diesel engine?
refused  (best distance 0.899)  Who won the 1994 World Cup?
refused  (best distance 0.846)  What is the recommended dosage of ibuprofen for a headache?
refused  (best distance 0.813)  How do I write a for loop in Rust?
-> gate refused 5 of 5
```

**Criterion 4 — Sampled chunks contain a complete section or thought**

Produced by `app.py chunks` using `chunker.py::split_documents`.

Runs 1, 2, and 3 scored 4/5, 5/5, and 5/5. The one chunk that did not meet the criterion was:

```text
Chunk 5 | source: guide_seasons.md#0 | produced by: chunker.py::split_documents

# When to visit the region
```

This chunk contains only a heading and does not provide a complete thought on its own.

**Criterion 5 — Answers contain the expected fact**

Produced by `run_eval.py::main` and `generate.py`.

All 5 questions contained their expected fact in all 3 runs. Example:

```text
Question: What are the recommended months to visit Halden Bay while avoiding the busiest summer period?

The recommended months to visit Halden Bay while avoiding the busiest summer period (July and August) are June and September (`guide_halden_bay.md`).
```
## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | All 5 test questions retrieved information containing the expected answer, exceeding the target of at least 4 of 5 in each run. |
| 2 | Every answer names a source | MET | All 15 generated answers across the 3 runs named at least one source document, meeting the 5 of 5 target in every run. |
| 3 | Relevance gate stops out-of-corpus questions | MET | The relevance gate refused all 5 out-of-scope questions, exceeding the target of at least 4 of 5. |
| 4 | Sampled chunks contain a complete section or thought | MET | The three chunk samples scored 4/5, 5/5, and 5/5. Each run therefore met the target of at least 4 of 5 complete chunks. |
| 5 | Answers contain the expected fact | MET | All 5 answers contained the expected fact from `questions.py` in all 3 runs, exceeding the target of at least 4 of 5. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->
No criteria were missed during the baseline evaluation, so there was no failed criterion to trace to a pipeline stage. However, the results revealed a weakness in Criterion 4 and the chunking stage.

Criterion 4 met its target in all three runs with scores of 4/5, 5/5, and 5/5, but one sampled chunk from `guide_seasons.md` contained only the heading `# When to visit the region`. This occurs because `chunker.py::split_documents` can preserve a document title as its own chunk when content following the title begins with a `##` section heading. Although the criterion allowed one incomplete chunk per sample, a heading-only chunk provides little useful context for retrieval or generation.

Based on this result, I would tighten Criterion 4 from requiring 4 of 5 sampled chunks to be complete thoughts to requiring all 5 of 5 sampled chunks to contain meaningful standalone information.

## The Improvement

**What I changed:**

I updated `chunker.py::split_documents` to prevent Markdown headings with no body text from being stored as standalone chunks. I added `has_body_text()` to check whether a section contains meaningful text beyond Markdown headings before adding it to the chunk list.

After re-indexing, the number of chunks decreased from 98 to 94, and the shortest chunk increased from 23 characters to 174 characters. Criterion 4 improved from 4/5, 5/5, and 5/5 before the change to 5/5 in all three runs after the change. The other four criteria continued to meet their targets.

**Why I picked it:**

Although all five baseline criteria were met, Criterion 4 revealed a weakness in the chunking stage. One sampled chunk from `guide_seasons.md` contained only the heading `# When to visit the region`, which provided no useful information on its own. I chose to address this issue because it was a specific weakness revealed by the baseline evaluation, and removing heading-only chunks could improve chunk quality without changing parts of the pipeline that were already performing well.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks contain a complete section or thought | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Answer contains the expected fact | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->
Yes. The change improved chunk quality without hurting the other parts of the system. Before the change, Criterion 4 scored 4/5, 5/5, and 5/5 because one sampled chunk contained only a Markdown heading. After the change, Criterion 4 scored 5/5 in all three runs. The number of chunks decreased from 98 to 94, and the shortest chunk increased from 23 to 174 characters. The other four criteria also continued to meet their targets, showing that the change fixed the identified chunking issue without reducing the system's overall performance.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->
## What's Still Broken

All five criteria met their targets after the improvement, but the evaluation only uses five in-scope questions and five out-of-scope questions. Because the test set is small, it does not cover every type of question a user could ask about the city guides.

The system also relies on a fixed relevance cutoff of 0.6. It successfully rejected all five out-of-scope questions in this evaluation, but a more ambiguous question could fall close to the cutoff and be incorrectly accepted or rejected.

If I continued working on the system, I would expand the evaluation set with more difficult and ambiguous questions before making additional changes to retrieval or the relevance threshold. I stopped after the chunking improvement because it fixed the specific weakness found in the baseline evaluation while all five criteria continued to meet their targets.

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
## What I'd Do Differently

If I started this project again, I would design a larger and more varied evaluation set earlier in the process. My five test questions worked well for checking whether the system could retrieve specific facts from different city guides, but they did not create many difficult retrieval cases.

I would also inspect the structure of the corpus more closely before implementing the chunker. My section-based strategy preserved meaningful sections well, but I did not initially account for document titles that appeared before the first `##` heading. Testing more edge cases in the chunk structure earlier would have revealed the heading-only chunks before the evaluation stage.
