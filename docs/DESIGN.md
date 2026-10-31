# Design record

## Decision

The same English relevance labels evaluate lexical overlap, MiniLM dense retrieval and reciprocal-rank fusion. Ranking failures are retained alongside Recall@5 and MRR.

## Failure model

Exact metric calculation on an intentional miss and second-rank hit, deterministic ties and required relevance labels. Local evaluation executes real embeddings.

## Tradeoffs

Six documents and six queries are deliberately small. Dense retrieval loads a model only in local mode. The shared ranker conventions also appear in Support RAG Desk; this repository isolates retrieval experiments.

## Next change to defend in review

Add realistic distractors, chunking experiments and held-out multilingual relevance labels.

## Reproducibility

`uv.lock` pins Python dependencies; the web lockfile pins the React build where present. Model-backed evaluations use a separately installed local service. Dataset examples are synthetic and intentionally small. Reported timing is a local observation, not a throughput SLA. Run `make test` after changing state transitions and `make eval` after changing decisions. Keep inference quality separate from deterministic invariant checks.
