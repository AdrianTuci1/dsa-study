#!/usr/bin/env python3
"""Trainer cu repetiție spațiată pentru tiparele DSA din acest repo.

Folosește banca de carduri din `cards.py` și salvează progresul în
`progress.json` (lângă acest fișier).

Utilizare:
    python3 learning/trainer.py                 # repetă cardurile scadente
    python3 learning/trainer.py --limit 10      # sesiune scurtă
    python3 learning/trainer.py --concept dp    # doar un concept (substring)
    python3 learning/trainer.py --new           # doar carduri noi (nevăzute)
    python3 learning/trainer.py --shuffle       # ordine amestecată
    python3 learning/trainer.py --stats         # statistici
    python3 learning/trainer.py --list          # listează cardurile
    python3 learning/trainer.py --print         # foaie de studiu, fără prompt
    python3 learning/trainer.py --verify        # verifică banca de carduri
    python3 learning/trainer.py --reset --yes   # șterge progresul

Notare, după ce vezi răspunsul:
    1 again  - nu mi-a venit (repet azi)
    2 hard   - greu, dar aproape
    3 good   - știu
    4 easy   - trivial
"""

import argparse
import json
import os
import random
import sys
from datetime import date, timedelta

from cards import CARDS, CONCEPT_KEYS, verify as verify_cards

HERE = os.path.dirname(os.path.abspath(__file__))
STATE_PATH = os.path.join(HERE, "progress.json")

GRADES = {"1": 0, "2": 1, "3": 2, "4": 3}
GRADE_LABEL = {0: "again", 1: "hard", 2: "good", 3: "easy"}


# ---------------------------------------------------------------------------
# Stare (progress.json)
# ---------------------------------------------------------------------------
def load_state():
    if not os.path.exists(STATE_PATH):
        return {}
    try:
        with open(STATE_PATH, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            raise ValueError("conținutul nu e un obiect JSON")
        return data
    except (OSError, ValueError) as exc:
        backup = STATE_PATH + ".corrupt"
        try:
            os.replace(STATE_PATH, backup)
        except OSError:
            pass
        print("! progress.json e invalid (%s) - a fost mutat în %s" % (exc, backup))
        return {}


def save_state(state):
    """Scrie atomic: un fișier temporar în același director, apoi replace."""
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=2, sort_keys=True)
        fh.write("\n")
    os.replace(tmp, STATE_PATH)


def new_state(grade, previous=None):
    """SM-2 simplificat: întoarce starea nouă a unui card după o notare."""
    previous = previous or {}
    ease = previous.get("ease", 2.5)
    reps = previous.get("reps", 0)
    interval = previous.get("interval", 0)
    lapses = previous.get("lapses", 0)

    if grade == 0:  # again: se reia de azi, ușurința scade puțin
        ease = max(1.3, ease - 0.2)
        reps = 0
        interval = 0
        lapses += 1
    else:
        reps += 1
        if grade == 1:  # hard
            ease = max(1.3, ease - 0.15)
            interval = 1 if interval < 1 else max(1, interval * 1.2)
        elif grade == 2:  # good
            interval = 1 if reps == 1 else max(2, interval * ease)
        else:  # easy
            ease = min(2.8, ease + 0.15)
            interval = 1 if reps == 1 else max(2, interval * ease * 1.3)

    due = date.today() + timedelta(days=round(interval))
    return {
        "ease": round(ease, 2),
        "reps": reps,
        "interval": round(interval, 1),
        "lapses": lapses,
        "due": due.isoformat(),
    }


# ---------------------------------------------------------------------------
# Selecția cardurilor
# ---------------------------------------------------------------------------
def filtered_cards(concept=None):
    cards = CARDS
    if concept:
        needle = concept.lower()

        def matches(card):
            haystack = " ".join((
                card["concept"],
                CONCEPT_KEYS.get(card["concept"], ""),
                card["id"],
            )).lower()
            return needle in haystack

        cards = [c for c in cards if matches(c)]
    return cards


def due_cards(state, cards, today=None, only_new=False):
    """Carduri scadente (întâi cele restante, apoi cele noi)."""
    today = today or date.today().isoformat()
    overdue, fresh = [], []
    for card in cards:
        st = state.get(card["id"])
        if st is None:
            fresh.append(card)  # nou: îl înveți o dată
        elif only_new:
            continue
        elif st.get("due", today) <= today:
            overdue.append(card)
    overdue.sort(key=lambda c: state[c["id"]].get("due", ""))
    return overdue + fresh


def next_due(state, cards):
    """Cea mai apropiată dată de repetare dintre cardurile date."""
    dates = [state[c["id"]]["due"] for c in cards if c["id"] in state]
    return min(dates) if dates else None


# ---------------------------------------------------------------------------
# Comenzi
# ---------------------------------------------------------------------------
def cmd_review(args):
    state = load_state()
    cards = filtered_cards(args.concept)
    if not cards:
        print("Niciun card pentru filtrul %r." % args.concept)
        return 1

    session = due_cards(state, cards, only_new=args.new)
    if args.shuffle:
        random.shuffle(session)
    if args.limit is not None:
        session = session[: args.limit]

    if not session:
        print("Nimic de repetat. %s" % ("Toate cardurile sunt la zi." if not args.new else "Nu ai carduri noi."))
        nxt = next_due(state, cards)
        if nxt:
            print("Următoarea repetare: %s" % nxt)
        return 0

    interactive = sys.stdin.isatty() and not args.print_mode
    if not interactive:
        print_sheet(session)
        return 0

    print("%d carduri în sesiune. Ctrl+C oricând (progresul se salvează).\n" % len(session))
    reviewed = 0
    try:
        for i, card in enumerate(session, 1):
            print("-" * 70)
            print("[%d/%d] %s   (%s)" % (i, len(session), card["id"], card["concept"]))
            print("  Î: %s" % card["front"])
            answer = input("  ENTER arată răspunsul...").strip().lower()
            if answer == "h" and card.get("hint"):
                print("  hint: %s" % card["hint"])
                input("  ENTER continuă...")
            print("  R: %s" % card["back"])
            while True:
                raw = input("  1 again / 2 hard / 3 good / 4 easy  > ").strip()
                if raw in GRADES:
                    break
                if raw in ("h", "hint"):
                    if card.get("hint"):
                        print("  hint: %s" % card["hint"])
                    continue
            st = new_state(GRADES[raw], state.get(card["id"]))
            state[card["id"]] = st
            save_state(state)
            reviewed += 1
            print("  ok -> următoarea repetare: %s (interval %.1f zile)\n" % (st["due"], st["interval"]))
    except KeyboardInterrupt:
        print("\nÎntrerupt.")

    print("=" * 70)
    print("Sesiune: %d carduri notate." % reviewed)
    nxt = next_due(state, cards)
    if nxt:
        print("Următoarea repetare: %s" % nxt)
    print("Statistici: python3 learning/trainer.py --stats")
    return 0


def print_sheet(session):
    """Mod neinteractiv: doar afișează întrebarea și răspunsul."""
    if not sys.stdin.isatty():
        print("(stdin nu e terminal -> afișez foaia de studiu în loc de quiz)\n")
    for i, card in enumerate(session, 1):
        print("-" * 70)
        print("[%d/%d] %s   (%s)" % (i, len(session), card["id"], card["concept"]))
        print("  Î: %s" % card["front"])
        print("  R: %s" % card["back"])
        if card.get("hint"):
            print("  hint: %s" % card["hint"])
    print("-" * 70)
    print("%d carduri. Rulează fără --print, într-un terminal, pentru quiz." % len(session))


def cmd_stats(args):
    state = load_state()
    today = date.today().isoformat()
    cards = filtered_cards(args.concept)
    buckets = {"new": 0, "learning": 0, "young": 0, "mature": 0}
    due_today = 0
    total_ease = 0.0
    with_state = 0
    per_concept = {}

    for card in cards:
        st = state.get(card["id"])
        if st is None:
            buckets["new"] += 1
        else:
            with_state += 1
            total_ease += st.get("ease", 2.5)
            if st.get("reps", 0) <= 1:
                buckets["learning"] += 1
            elif st.get("interval", 0) < 21:
                buckets["young"] += 1
            else:
                buckets["mature"] += 1
            if st.get("due", today) <= today:
                due_today += 1
        if st is None or st.get("due", today) <= today:
            per_concept[card["concept"]] = per_concept.get(card["concept"], 0) + 1

    print("Carduri: %d   (filtrate după: %s)" % (len(cards), args.concept or "toate"))
    print("  noi:       %d" % buckets["new"])
    print("  learning:  %d" % buckets["learning"])
    print("  young:     %d" % buckets["young"])
    print("  mature:    %d" % buckets["mature"])
    print("  de repetat azi: %d" % due_today)
    if with_state:
        print("  ease mediu: %.2f" % (total_ease / with_state))

    if per_concept:
        print("\nRămase azi (noi + scadente), pe concept:")
        for concept in sorted(per_concept):
            print("  %-28s %2d" % (concept, per_concept[concept]))

    nxt = next_due(state, cards)
    print("\nUrmătoarea repetare: %s" % (nxt or "-"))
    return 0


def cmd_list(args):
    cards = filtered_cards(args.concept)
    state = load_state()
    for card in cards:
        st = state.get(card["id"])
        if st is None:
            when = "nou"
        else:
            when = "scadent %s" % st.get("due", "?")
        print("%-6s %-26s %-14s %s" % (card["id"], card["concept"], when, card["front"][:70]))
    print("\n%d carduri." % len(cards))
    return 0


def cmd_verify(args):
    problems = verify_cards()
    ids = set()
    for card in CARDS:
        if card["id"] in ids:
            problems.append("id duplicat: %s" % card["id"])
        ids.add(card["id"])
    if problems:
        print("Banca de carduri are probleme:")
        for p in problems:
            print("  -", p)
        return 1
    print("OK: %d carduri valide." % len(CARDS))
    return 0


def cmd_reset(args):
    if not args.yes:
        raw = input("Ștergi tot progresul (%s)? scrie 'yes': " % STATE_PATH).strip().lower()
        if raw != "yes":
            print("Anulat.")
            return 1
    if os.path.exists(STATE_PATH):
        os.remove(STATE_PATH)
        print("Progres șters.")
    else:
        print("Nu există progres salvat.")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Repetiție spațiată pentru tiparele DSA (learning area).",
    )
    parser.add_argument("--concept", help="filtrează după concept (substring, ex: dp, trie)")
    parser.add_argument("--limit", type=int, default=20, help="câte carduri într-o sesiune (implicit 20)")
    parser.add_argument("--new", action="store_true", help="doar carduri noi (nevăzute)")
    parser.add_argument("--shuffle", action="store_true", help="amestecă ordinea")
    parser.add_argument("--print", dest="print_mode", action="store_true",
                        help="afișează foaia de studiu fără să ceri input")
    parser.add_argument("--stats", action="store_true", help="statistici de progres")
    parser.add_argument("--list", dest="list_cards", action="store_true", help="listează cardurile")
    parser.add_argument("--verify", action="store_true", help="verifică banca de carduri")
    parser.add_argument("--reset", action="store_true", help="șterge progresul")
    parser.add_argument("--yes", action="store_true", help="confirmă --reset fără întrebare")
    args = parser.parse_args(argv)

    if args.list_cards:
        return cmd_list(args)
    if args.stats:
        return cmd_stats(args)
    if args.verify:
        return cmd_verify(args)
    if args.reset:
        return cmd_reset(args)
    return cmd_review(args)


if __name__ == "__main__":
    raise SystemExit(main())
