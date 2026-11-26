# Study app

A small web app for active recall: 114 drills across 30 DSA patterns, plus
101 problems in a two-pane Solve workspace (14 curated with variants and 87
parsed from `practice/*.py`). Spaced repetition, dark mode,
a canvas knowledge graph, no dependencies.

The app does **not** bundle content. A tiny Python server reads the source
files and serves them from `/api/content`; the app fetches that JSON at boot.

```bash
python3 learning/study/serve.py          # default port 8765
# open http://127.0.0.1:8765/
```

Opening `index.html` directly does not work: the browser cannot fetch the
content API from `file://`. The page explains this and prints the command.

## What a session looks like

A session mixes four drill types:

| Type | You do | Graded by |
|---|---|---|
| Recall | Answer a question from memory, then reveal | You (Again / Hard / Good / Easy) |
| Multiple choice | Pick the correct rule or complexity | App |
| Fill the blank | Type the missing line of a template | App (normalised match) |
| Predict output | Read a snippet and type what it evaluates to | App |

Wrong typed answers show what you wrote, the expected answer and the reason.
If your answer was right but spelled differently, you can mark it equivalent.

## Solve workspace

The **Solve** tab is a two-pane page for working through full problems:

- **Left:** the problem statement, examples and constraints, rendered as a
  document with inline code and Python syntax highlighting.
- **Toggle:** `Show solution` reveals the solution variants. Each variant has
  its name, complexity and a short note explaining why it works.
- **Sources:** the `Curated` tab uses `solve_bank.py` (multiple variants);
  the `practice/` tab reads the problem statements, examples, constraints and
  your own function from `practice/*.py` at request time.
- **Right:** your sheet. A monospace editor with live syntax highlighting,
  line numbers and autosave per problem in `localStorage`. `Mark solved`
  tracks completion.
- **Run tests:** for `practice/` problems, the sheet is executed against the
  tests in that practice file (subprocess, CPU and time limit) and the panel
  shows `passed / total` plus expected vs. got. The practice file's top-level
  imports (`heapq`, `deque`, ...) are available to the sheet, so you only write
  the function.

The two panes scroll independently on desktop and stack on narrow screens. The
sheet keeps its own text per problem; switching problems or reloading does not
lose it.

`Run tests` executes code locally. The server binds `127.0.0.1` by default;
never expose it (or the Docker port) publicly.

## Cheatsheet

The **Cheatsheet** tab holds 31 sections in 8 groups: essentials, patterns,
graphs, DP, structures, matrix & bits, strings, and meta. Each section is a
short template with a note. The search box filters by title, tag, note, code or
table.

The content lives in `learning/study/cheatsheet.json`; edit it and reload.

## Knowledge graph

The **Graph** tab draws the 30 concepts on a canvas:

- nodes are concepts; edges are "learn this after that" links
- the bar under each node is `reviewed items / total items` for that concept
- hover a node for the exact numbers; click it to start a drill session
  filtered to that concept
- on narrow screens the canvas scrolls horizontally instead of shrinking the
  text into unreadable dots

The layout lives in `graph.json` (`nodes`, `edges`, `layer`). Edit it and
reload: the server re-reads the file. Progress is not stored there; it is
derived from the drill bank and your saved review progress.

## Spaced repetition

Every drill is a card with `ease`, `interval`, `reps`, `lapses` and `due`.
Grades map to a small SM-2 variant:

- **again** (1): back today, ease decreases
- **hard** (2): about a day
- **good** (3): interval multiplied by ease (1, 2.5, 6, 15... days)
- **easy** (4): faster growth, ease increases

The dashboard shows what is due, what is new, what is in progress and what is
mastered (interval >= 21 days), plus a daily streak. The default daily goal is
20 reviews and can be changed on the home page.

## Keys

| Key | Action |
|---|---|
| `space` | primary action: reveal, check, next |
| `1`–`4` | grade a recall card, or pick an option |
| `enter` | check a typed answer |
| `escape` | back to home |

In the Solve sheet, `Tab` inserts four spaces and `Enter` keeps the current
indentation, so you can type Python without fighting the focus.

## Theme

The checkbox in the topbar switches between light and dark. The choice is
remembered per browser (`dsa-study-theme`). Until you toggle it, the app
follows the OS `prefers-color-scheme` setting. The theme is applied before
first paint, so there is no light flash on reload.

## Where the content lives

```
learning/
├── content.py           reads and validates the source files
├── study_bank.py        recall items (question / answer)
├── study_extras.py      choice / code / trace drills
├── solve_bank.py        14 problems with solution variants
├── build_study.py       validation CLI (writes nothing)
└── study/
    ├── serve.py         static files + /api/content + /api/run
    ├── run_practice.py  executes a sheet against practice tests
    ├── graph.json       knowledge graph layout (nodes and edges)
    ├── cheatsheet.json  31 sections, grouped
    ├── index.html       the app shell
    ├── style.css        minimal UI
    ├── core.js          scheduling, selection, stats (no DOM)
    ├── app.js           views and events
    └── test_core.js     node tests for core.js
```

There is **no build step**. `serve.py` rebuilds `/api/content` from the files
on every request, so you edit a source file and reload the page:

- drills: `study_bank.py`, `study_extras.py`
- curated problems and solution variants: `solve_bank.py`
- practice problems (statement + your solution): `practice/*.py`
- cheat sheet: `cheatsheet.json`
- graph layout and edges: `graph.json`

Validate everything without starting the server:

```bash
python3 learning/build_study.py
```

The validator checks ids, concepts, option counts, that every code drill has
exactly one `___`, that every problem variant parses as Python (via `ast`),
that every cheat sheet section has a group/title/note and a code block or a
3-column table, and it executes every trace `setup`/`expr` to compute the
answer key. A trace
answer can never drift from the code it shows. The same validation runs
inside the server: if a source file is broken, the app shows the exact list of
problems instead of a blank page.

Run the logic tests:

```bash
node learning/study/test_core.js
```

## Adding a drill

Recall card in `study_bank.py`:

```python
recall(
    "r-17-06", "17 Dynamic Programming",
    "Interval DP: how do you order the loops?",
    "By interval length, increasing, then pick a split point k.",
)
```

Choice drill in `study_extras.py`:

```python
{
    "id": "ch-19",
    "concept": "09 Binary Search",
    "type": "choice",
    "question": "...",
    "options": ["...", "...", "...", "..."],
    "answer": 0,
    "explain": "...",
}
```

Code drill: include exactly one `___` in `code` and list accepted variants in
`answers`. Trace drill: provide `setup` and `expr`; the builder computes the
answer.

Then reload the page: the server re-reads the file.

## Progress

Progress is stored in `localStorage` under `dsa-study-v1`; your Solve sheets
live under `dsa-study-notes` and the last opened problem under
`dsa-study-problem`.

- **Export** downloads a JSON file; **Import** restores it.
- **Reset** clears the review progress (sheets are kept; clear them with the
  sheet's own Reset button).
- Serve the app through `learning/study/serve.py`: `localStorage` is available
  on the HTTP origin. A plain `python3 -m http.server` is not enough because the
  app needs `/api/content`.

The app is English on purpose: the drills are interview-shaped.
