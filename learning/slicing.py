#!/usr/bin/env python3
"""Laborator de slicing: prezice output-ul, apoi vezi explicația.

Răspunsurile sunt calculate cu Python la rulare (`eval` pe expresii literale),
deci nu pot fi greșite sau desincronizate de explicații.

Utilizare:
    python3 learning/slicing.py            # quiz interactiv
    python3 learning/slicing.py --limit 8  # doar 8 exerciții
    python3 learning/slicing.py --answers  # tabelul complet, fără quiz
    python3 learning/slicing.py --verify   # self-check al exercițiilor

Ideea din spate: `a[start:stop:step]` produce un obiect NOU de același tip
(copie superficială), iar `a[1][:]` se citește stânga->dreapta: `a[1]`, apoi
`[:]`. Detalii în learning/PYTHON_SLICING.md.
"""

import argparse
import random
import sys

# ---------------------------------------------------------------------------
# Namespace-ul exercițiilor
# ---------------------------------------------------------------------------
argument = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [10, 20, 30, 40, 50]
word = "python"
matrix = [[1, 2], [3, 4]]

NAMESPACE = {
    "argument": argument,
    "flat": flat,
    "word": word,
    "matrix": matrix,
    "len": len,
}

# (expresie, explicație)
EXERCISES = [
    ("argument[:1]",
     "Felie de la 0 până la 1 (exclusiv) -> listă cu PRIMUL element al lui "
     "argument. Nu e „elementul 1”."),
    ("argument[1]",
     "Elementul de pe poziția 1: al doilea rând."),
    ("argument[1][:]",
     "Stânga->dreapta: întâi argument[1], apoi [:] pe el -> copie a rândului 1."),
    ("argument[1][:1]",
     "argument[1] = rândul 1; [:1] ia primul lui element, dar ca felie -> listă."),
    ("argument[1][:][0]",
     "argument[1] -> rândul 1; [:] -> copie; [0] -> primul element al copiei."),
    ("argument[:1][0]",
     "Prima felie -> [rândul 0]; apoi [0] -> rândul 0 întreg."),
    ("argument[:][1]",
     "[:] copiază lista exterioară; [1] ia al doilea rând (aceleași obiecte)."),
    ("argument[:2][1]",
     "Primele două rânduri, apoi al doilea dintre ele."),
    ("argument[-1][::-1]",
     "Ultimul rând, inversat."),
    ("flat[:1]",
     "Primul element, ca listă."),
    ("flat[1:]",
     "De la indexul 1 până la capăt."),
    ("flat[:]",
     "Copie superficială a listei."),
    ("flat[::2]",
     "Din 2 în 2, de la început."),
    ("flat[::-1]",
     "Pas negativ -> lista inversată (copie)."),
    ("flat[-1]",
     "Ultimul element (index negativ)."),
    ("flat[-2:]",
     "Ultimele două elemente."),
    ("flat[1:4]",
     "Indexii 1, 2, 3 (stop exclusiv)."),
    ("flat[4:1]",
     "start după stop, pas pozitiv -> felie goală."),
    ("flat[100:]",
     "Limitele se taie la capăt; slicing-ul nu aruncă IndexError."),
    ("flat[:0]",
     "De la 0 până la 0 -> listă goală."),
    ("flat[:1] + flat[-1:]",
     "Concatenare de liste."),
    ("len(flat[:1])",
     "Lungimea feliei cu un element."),
    ("flat[:] is flat",
     "[:] creează listă nouă -> nu e același obiect (False)."),
    ("argument[:] is argument",
     "La fel: felia completă e o listă nouă (False)."),
    ("argument[:][0] is argument[0]",
     "Shallow: elementele sunt ACELEAȘI obiecte -> True."),
    ("argument[1][:] is argument[1]",
     "Rândul copiat e un obiect nou -> False."),
    ("word[:1]",
     "Pe string, felia e tot string (aici de lungime 1)."),
    ("word[1][:]",
     "word[1] e 'y' (string); [:] pe un string returnează același string."),
    ("word[:3][1]",
     "Primele 3 caractere 'pyt', apoi al doilea -> 'y'."),
    ("word[::-1]",
     "Stringul inversat."),
    ("word[-1]",
     "Ultimul caracter."),
    ("word[2:5]",
     "Caracterele de la 2 la 4."),
    ("word[5:2]",
     "start după stop -> string gol."),
    ("word[1:3] + word[-1]",
     "Concatenare de stringuri."),
    ("[row[:] for row in matrix]",
     "Copie pe două niveluri: listă nouă de rânduri noi."),
    ("matrix[:]",
     "Doar nivelul exterior: listă nouă, dar aceleași rânduri."),
]


def value_of(expr):
    return eval(expr, {"__builtins__": {}}, NAMESPACE)


def normalize(text):
    """Compară tolerant la spații; acceptă și string fără ghilimele."""
    return "".join(str(text).split())


def accepted_answers(value):
    return {normalize(repr(value)), normalize(str(value))}


def is_correct(given, value):
    return normalize(given) in accepted_answers(value)


def show_table(limit=None):
    items = EXERCISES[:limit] if limit else EXERCISES
    for expr, why in items:
        value = value_of(expr)
        print("%-34s -> %s" % (expr, repr(value)))
        print("    %s" % why)
    print("\n%d exerciții." % len(items))


def run_quiz(limit=None, shuffle=False):
    items = list(EXERCISES)
    if shuffle:
        random.shuffle(items)
    if limit is not None:
        items = items[:limit]

    correct = 0
    print("Completează output-ul. ENTER = arată răspunsul, q = ieși.\n")
    for i, (expr, why) in enumerate(items, 1):
        value = value_of(expr)
        print("[%d/%d] %s   -> ?" % (i, len(items), expr))
        try:
            given = input("  răspuns: ")
        except EOFError:
            print("\n(stdin închis -> afișez restul ca tabel)\n")
            show_table(limit)
            return 0
        if given.strip().lower() in ("q", "quit", "exit"):
            print("La revedere.")
            break
        if given.strip() == "":
            print("  (reveal) %r" % (value,))
        elif is_correct(given, value):
            correct += 1
            print("  [v] corect: %r" % (value,))
        else:
            print("  [x] ai scris %r, corect era %r" % (given.strip(), value))
        print("  de ce: %s\n" % why)

    total = len(items)
    print("=" * 70)
    print("Scor: %d/%d" % (correct, total))
    if correct < total:
        print("Reia cu: python3 learning/slicing.py --limit 8")
        print("Teorie:  learning/PYTHON_SLICING.md")
    return 0


def verify():
    problems = []
    for expr, why in EXERCISES:
        if not why:
            problems.append("explicație lipsă pentru %r" % expr)
        try:
            value_of(expr)
        except Exception as exc:  # noqa: BLE001 - raportăm explicit
            problems.append("%r nu se poate evalua: %s" % (expr, exc))
    if problems:
        print("Laboratorul are probleme:")
        for p in problems:
            print("  -", p)
        return 1
    print("OK: %d exerciții valide." % len(EXERCISES))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Laborator interactiv de slicing Python.")
    parser.add_argument("--limit", type=int, help="câte exerciții")
    parser.add_argument("--shuffle", action="store_true", help="amestecă ordinea")
    parser.add_argument("--answers", action="store_true", help="afișează tabelul cu răspunsuri")
    parser.add_argument("--verify", action="store_true", help="self-check")
    args = parser.parse_args(argv)

    if args.verify:
        return verify()
    if args.answers:
        show_table(args.limit)
        return 0
    if not sys.stdin.isatty():
        print("(stdin nu e terminal -> afișez tabelul în loc de quiz)\n")
        show_table(args.limit)
        return 0
    return run_quiz(args.limit, args.shuffle)


if __name__ == "__main__":
    raise SystemExit(main())
