# Pregătire pentru interviu — RAG Retrieval Lab

Roluri țintă: RAG / Search / Evaluation.

## Prezentare de 90 de secunde

1. Explică problema concretă și cine folosește rezultatul.
2. Rulează `make demo` sau fluxul din UI.
3. Arată testul pentru un caz de eșec, apoi explică mecanismul din cod.
4. Spune ce limite are demonstrația și ce ai construi pentru producție.

Decizia de explicat: The same English relevance labels evaluate lexical overlap, MiniLM dense retrieval and reciprocal-rank fusion. Ranking failures are retained alongside Recall@5 and MRR.

## Cinci întrebări

1. Ce măsoară MRR?
2. De ce Recall@5 poate arăta bine pe un corpus mic?
3. Cum funcționează RRF?
4. Cum alegi chunk size?
5. Cum construiești relevance labels?

## Exercițiu înainte de a aplica

Add realistic distractors, chunking experiments and held-out multilingual relevance labels.

Alege o parte mică a acestei modificări, implementeaz-o personal, adaugă un test care verifică comportamentul și descrie rezultatul într-un commit real. Nu declara că ai înțeles sau construit singur o parte pe care nu o poți explica.

## Checklist personal

- [ ] Pot porni proiectul dintr-un checkout curat.
- [ ] Pot urmări cererea până la rezultatul salvat.
- [ ] Pot explica diferența dintre fixture și model local.
- [ ] Pot demonstra un eșec și recuperarea lui.
- [ ] Am făcut o modificare proprie și o pot explica în engleză.

Aceste puncte necesită review-ul tău; nu au fost bifate automat.
