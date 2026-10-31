import pytest
from app.core import benchmark
from app.retrieval import lexical


def test_metrics_with_miss_and_second_rank():
    docs = [{"id": "a", "text": "alpha"}, {"id": "b", "text": "beta"}]
    r = benchmark(
        docs, [{"query": "alpha", "relevant": ["b"]}, {"query": "other", "relevant": ["missing"]}], "lexical"
    )
    assert r["mrr"] == 0.25 and r["recall_at_5"] == 0.5
    assert len(r["failures"]) == 2


def test_deterministic_ties_and_unknown_relevance():
    assert lexical("nonsense", [{"id": "b", "text": "x"}, {"id": "a", "text": "x"}])[0][0]["id"] == "a"
    with pytest.raises(ValueError):
        benchmark([{"id": "a", "text": "x"}], [{"query": "x", "relevant": []}], "lexical")
