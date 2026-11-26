# Learning area — memorare prin recall activ

Aici **memorezi** tiparele, ca să nu le re-deduci de la zero la interviu.
`practice/` e locul unde **scrii cod**; `learning/` e locul unde **verifici ce
știi din memorie**, zilnic, în 10-15 minute.

Patru lucruri, fiecare cu un singur scop:

| Ce folosești | Ce faci | Cui se adresează |
|---|---|---|
| `study/` (aplicația) | sesiuni mixte (114 exerciții), workspace Solve (14 probleme + variante) și graf de cunoștințe pe canvas, citite din fișiere | exersatul zilnic, vizual |
| `trainer.py` + `cards.py` | flashcard-uri în terminal cu repetiție spațiată (96 carduri) | când vrei rapid, fără browser |
| `slicing.py` | quiz „prezice output-ul" pentru felii Python (36 exerciții) | sintaxa care produce bug-uri |
| `PYTHON_SLICING.md` | explicația `a[:1]`, `a[1][:]`, copii superficiale | citit o dată, apoi exersat |

> Aplicația din `study/` este în **engleză** (limba interviului) și își ține
> progresul în browser. Detalii: [`study/README.md`](./study/README.md).

## Pornire rapidă

```bash
# 0. Aplicația (recomandat pentru sesiunea zilnică)
#    Serverul citește conținutul din study_bank.py / study_extras.py /
#    solve_bank.py / graph.json la fiecare request; nu există build step.
python3 learning/study/serve.py
# apoi deschide http://127.0.0.1:8765/ (sau /#solve, /#graph)

# 1. Ce ai de repetat azi, în terminal (întâi restanțele, apoi carduri noi)
python3 learning/trainer.py

# 2. Sesiune scurtă, doar un concept
python3 learning/trainer.py --concept dp --limit 10

# 3. Slicing: prezice output-ul
python3 learning/slicing.py

# 4. Starea progresului
python3 learning/trainer.py --stats
```

Dacă rulezi într-un mediu fără terminal interactiv, `trainer.py` afișează
automat foaia de studiu (întrebare + răspuns) în loc să ceară input. Forțat:
`--print`.

## Cum funcționează repetiția spațiată

După ce vezi răspunsul, notezi cardul cu o tastă:

| Tastă | Notă | Efect |
|---|---|---|
| `1` | again | se repetă azi, ușurința scade |
| `2` | hard | se repetă mâine, creștere lentă |
| `3` | good | interval × ușurință (1, 2.5, 6, 15... zile) |
| `4` | easy | creștere mai agresivă |

Fiecare card are `ease` (1.3–2.8), `interval` (zile), `reps`, `lapses` și `due`.
Progresul se salvează în `learning/progress.json` după **fiecare** notare, deci
poți întrerupe oricând cu Ctrl+C fără să pierzi nimic. Fișierul e local — dacă
vrei să o iei de la zero: `python3 learning/trainer.py --reset --yes`.

## Ritualul zilnic (recomandat)

1. **5 min** — `python3 learning/trainer.py --limit 10` (doar cardurile scadente).
2. **5 min** — `python3 learning/slicing.py --limit 6` sau un card greșit reluat.
3. **20-30 min** — un fișier din `practice/` (scrii soluția, nu o citești).
4. La final, dacă ai greșit ceva în practice, transformă greșeala într-un card
   nou în `cards.py` — asta e bucla care contează.

Regula de aur: **încearcă să răspunzi înainte să dai ENTER.** Recunoașterea
(„a, da, știu") nu e recall. Dacă nu-ți vine în 10 secunde, notează `1` sau `2`.

## Structura

```
learning/
├── README.md            → fișierul de față
├── PYTHON_SLICING.md    → teoria felilor, cu exemple și capcane
├── cards.py             → banca de carduri pentru CLI (română) + `verify()`
├── trainer.py           → motorul CLI de repetiție spațiată
├── slicing.py           → laborator interactiv de slicing (răspunsuri calculate live)
├── content.py           → citește și validează fișierele sursă
├── study_bank.py        → cardurile de recall pentru aplicație (engleză)
├── study_extras.py      → exercițiile choice / code / trace pentru aplicație
├── solve_bank.py        → problemele din workspace-ul Solve + variante
├── build_study.py       → CLI de validare (nu scrie nimic)
├── study/               → aplicația + serverul (`serve.py`), graful (`graph.json`)
└── progress.json        → creat automat de trainer; progresul tău (nu-l edita)
```

## Cardurile

Sunt grupate pe conceptele din `practice/` (01–29) plus `00 Python esențial`.
Cele mai importante sunt cele de **recunoaștere**: „ce tipar e ăsta și ce
skeleton are", nu detaliile de sintaxă.

Exemple de ce întreabă:

- „Bellman-Ford cu cel mult K opriri: de ce copiezi distanțele?"
- „De ce bucla pe capacitate la knapsack 1-D merge descrescător?"
- „Ce face `a[:1]` și ce face `a[1]`?"

Filtrează după concept cu substring: `--concept dp`, `--concept trie`,
`--concept python`, `--concept grafuri`.

### Adaugi un card

Lipește în `CARDS` din `cards.py`:

```python
card(
    "17-06", "17 Dynamic Programming",
    "Întrebarea (front)?",
    "Răspunsul scurt, cu skeletonul (back).",
    "indiciu opțional",
),
```

Apoi verifică: `python3 learning/trainer.py --verify` (id unic, câmpuri
necompletate, etc.). Nu e nevoie să numerotezi perfect — id-ul trebuie doar
unic.

## De ce nu e totul în `practice/`?

`practice/` are 3 probleme per concept și îți cere să scrii soluția întreagă.
Asta e excelent, dar lent: într-o zi de 20 de minute nu prinzi destule tipare.
Cardurile izolează **decizia** („ce structură, ce recurență, ce complexitate")
și o repeți până devine automatism. Când memoria e acolo, `practice/` devine
exersare de scris cod, nu de gândit de la zero.

## Legături

- [`../practice/README.md`](../practice/README.md) — exerciții de scris cod.
- [`../TEHNICI.md`](../TEHNICI.md) — teoria lungă, pe capitole (cardurile trimit la ea).
- [`../STRUCTURI.md`](../STRUCTURI.md) — structurile de date.
- [`../STUDY_PLAN.md`](../STUDY_PLAN.md) — planul și ritmul general.
