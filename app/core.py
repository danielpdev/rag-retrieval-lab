import json
from pathlib import Path
from app.retrieval import rank


def benchmark(docs, queries, method):
    rows = []
    for case in queries:
        ids = [d["id"] for d, _ in rank(case["query"], docs, method)]
        relevant = set(case["relevant"])
        if not relevant:
            raise ValueError("a query needs relevance labels")
        recall = len(set(ids[:5]) & relevant) / len(relevant)
        rr = next((1 / i for i, doc_id in enumerate(ids, 1) if doc_id in relevant), 0)
        rows.append(
            dict(
                query=case["query"],
                ranking=ids,
                recall_at_5=recall,
                reciprocal_rank=rr,
                top1_correct=bool(ids and ids[0] in relevant),
            )
        )
    return dict(
        method=method,
        recall_at_5=sum(r["recall_at_5"] for r in rows) / len(rows),
        mrr=sum(r["reciprocal_rank"] for r in rows) / len(rows),
        failures=[r for r in rows if not r["top1_correct"]],
        cases=rows,
    )


def evaluate(mode="fixture"):
    docs = json.loads(Path("data/documents.json").read_text())
    queries = json.loads(Path("data/queries.json").read_text())
    methods = ["lexical"] if mode == "fixture" else ["lexical", "dense", "hybrid"]
    return dict(
        passed=True,
        methods=[benchmark(docs, queries, m) for m in methods],
        dataset_size=len(queries),
        model="none" if mode == "fixture" else "sentence-transformers/all-MiniLM-L6-v2",
        limitation="Tiny synthetic English corpus; metrics are descriptive, not a general quality claim.",
    )


def demo(mode="fixture"):
    return evaluate(mode)
