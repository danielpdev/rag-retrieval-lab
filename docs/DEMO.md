# Demo walkthrough

## Start

```bash
make setup
make demo
make test
make eval
```

## What to show

The same English relevance labels evaluate lexical overlap, MiniLM dense retrieval and reciprocal-rank fusion. Ranking failures are retained alongside Recall@5 and MRR.

## Failure case to discuss

Exact metric calculation on an intentional miss and second-rank hit, deterministic ties and required relevance labels. Local evaluation executes real embeddings.

## Evidence

Open the JSON evaluation report alongside the implementation. Distinguish synthetic fixture outputs, synthetic trace timing, actual elapsed evaluation time, and local model inference. Do not present a tiny test set as a production benchmark.

## Closing tradeoff

Six documents and six queries are deliberately small. Dense retrieval loads a model only in local mode. The shared ranker conventions also appear in Support RAG Desk; this repository isolates retrieval experiments.

The repository's `docs/demo.webm` or `docs/demo.mp4`, when present, records the demonstration. A terminal replay is also available for focused projects as `docs/demo.cast`.
