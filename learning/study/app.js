/* DSA Study — UI.
 *
 * Views: home (dashboard), session (mixed drills), cheatsheet (templates).
 * All logic that does not touch the DOM lives in core.js.
 */
(function () {
  "use strict";

  const core = window.StudyCore;
  let ITEMS = [];
  let PROBLEMS = [];
  let PRACTICE = [];
  let GRAPH = { nodes: [], edges: [] };
  let CONCEPTS = [];
  let CHEATS = [];
  const STORAGE_KEY = "dsa-study-v1";
  const THEME_KEY = "dsa-study-theme";
  const NOTES_KEY = "dsa-study-notes";
  const PROBLEM_KEY = "dsa-study-problem";
  const TYPE_LABEL = {
    recall: "recall",
    choice: "multiple choice",
    code: "fill the blank",
    trace: "predict output",
  };
  const LETTERS = ["A", "B", "C", "D", "E", "F"];

  const state = {
    view: "home",
    progress: null,
    session: null,
    card: null,
    notes: {},
    solve: { source: "curated", index: 0, solutionOpen: false, variant: 0 },
    canStore: true,
    loaded: false,
    lastView: null,
  };

  const els = {
    view: document.getElementById("view"),
    streak: document.getElementById("streakBadge"),
    footLeft: document.getElementById("footLeft"),
    footRight: document.getElementById("footRight"),
  };

  // ---------------------------------------------------------------- utils
  function esc(value) {
    return String(value == null ? "" : value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  const PY_KEYWORDS = new Set([
    "def", "class", "return", "if", "elif", "else", "for", "while", "in",
    "not", "and", "or", "is", "None", "True", "False", "import", "from",
    "as", "with", "try", "except", "finally", "raise", "yield", "lambda",
    "pass", "break", "continue", "global", "nonlocal", "assert", "del",
    "async", "await",
  ]);

  const PY_BUILTINS = new Set([
    "len", "range", "min", "max", "sum", "sorted", "enumerate", "zip", "map",
    "filter", "reversed", "set", "dict", "list", "tuple", "int", "str",
    "float", "bool", "abs", "any", "all", "isinstance", "type", "print",
    "round", "divmod", "open", "input", "deque", "heapq", "heappush",
    "heappop", "heapify", "bisect_left", "bisect_right", "Counter",
    "defaultdict", "OrderedDict", "lru_cache", "product", "accumulate",
  ]);

  // Small Python tokenizer: comments, strings, decorators, def/class names,
  // keywords, builtins, numbers and operators. No dependency, no DOM.
  function highlightPython(code) {
    const pattern = /(#[^\n]*)|("""[\s\S]*?"""|'''[\s\S]*?'''|(?:[rRbBuUfF]{0,2})?(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'))|(@[A-Za-z_]\w*)|\b(def|class)\s+([A-Za-z_]\w*)|\b([A-Za-z_]\w*)\b|\b(\d[\d_]*(?:\.\d+)?)\b|([+\-*/%=<>!&|^~]+)/g;
    let out = "";
    let last = 0;
    let match;
    while ((match = pattern.exec(code)) !== null) {
      out += esc(code.slice(last, match.index));
      if (match[1]) {
        out += '<span class="tok-comment">' + esc(match[1]) + "</span>";
      } else if (match[2]) {
        out += '<span class="tok-string">' + esc(match[2]) + "</span>";
      } else if (match[3]) {
        out += '<span class="tok-decorator">' + esc(match[3]) + "</span>";
      } else if (match[4]) {
        out += '<span class="tok-keyword">' + esc(match[4]) + "</span> " +
          '<span class="tok-function">' + esc(match[5]) + "</span>";
      } else if (match[6]) {
        if (PY_KEYWORDS.has(match[6])) {
          out += '<span class="tok-keyword">' + esc(match[6]) + "</span>";
        } else if (PY_BUILTINS.has(match[6])) {
          out += '<span class="tok-builtin">' + esc(match[6]) + "</span>";
        } else {
          out += esc(match[6]);
        }
      } else if (match[7]) {
        out += '<span class="tok-number">' + esc(match[7]) + "</span>";
      } else {
        out += '<span class="tok-operator">' + esc(match[8]) + "</span>";
      }
      last = pattern.lastIndex;
    }
    out += esc(code.slice(last));
    return out;
  }

  function codeHtml(code) {
    return highlightPython(code).replace(/___/g, '<span class="blank">___</span>');
  }

  // Backtick spans become inline code. esc() runs first, so this stays safe.
  function richText(value) {
    return esc(value).replace(/`([^`]+)`/g, "<code>$1</code>");
  }

  function inlineMd(value) {
    return richText(value).replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  }

  // Minimal markdown: paragraphs and dash lists, with inline code and bold.
  function markdown(text) {
    return String(text)
      .split(/\n{2,}/)
      .map(function (block) {
        const lines = block
          .split("\n")
          .map(function (line) { return line.trim(); })
          .filter(Boolean);
        if (!lines.length) return "";
        if (lines.every(function (line) { return /^[-*]\s+/.test(line); })) {
          return '<ul class="md-list">' + lines
            .map(function (line) {
              return "<li>" + inlineMd(line.replace(/^[-*]\s+/, "")) + "</li>";
            })
            .join("") + "</ul>";
        }
        return "<p>" + inlineMd(lines.join(" ")) + "</p>";
      })
      .join("");
  }

  function codeBlock(code, muted) {
    return '<pre class="code-block' + (muted ? " code-block--muted" : "") + '">' + codeHtml(code) + "</pre>";
  }

  function detectStorage() {
    try {
      const key = "__dsa_study_test__";
      window.localStorage.setItem(key, "1");
      window.localStorage.removeItem(key);
      return true;
    } catch (err) {
      return false;
    }
  }

  function loadProgress() {
    if (!state.canStore) return core.emptyProgress();
    try {
      const raw = window.localStorage.getItem(STORAGE_KEY);
      return core.ensureProgress(raw ? JSON.parse(raw) : core.emptyProgress());
    } catch (err) {
      return core.emptyProgress();
    }
  }

  function saveProgress() {
    if (!state.canStore) return;
    try {
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(state.progress));
    } catch (err) {
      /* storage full or blocked; the session still works in memory */
    }
  }

  // ---------------------------------------------------------------- theme
  function currentTheme() {
    return document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
  }

  function applyTheme(theme, persist) {
    const dark = theme === "dark";
    document.documentElement.setAttribute("data-theme", dark ? "dark" : "light");
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", dark ? "#0b0b0d" : "#ffffff");
    const button = document.getElementById("themeToggle");
    if (button) button.setAttribute("aria-pressed", dark ? "true" : "false");
    if (persist) {
      try {
        window.localStorage.setItem(THEME_KEY, dark ? "dark" : "light");
      } catch (err) {
        /* theme still applies for this tab */
      }
    }
    if (state.view === "graph") drawGraph();
  }

  function initTheme() {
    applyTheme(currentTheme(), false);

    const button = document.getElementById("themeToggle");
    if (button) {
      button.addEventListener("click", function () {
        applyTheme(currentTheme() === "dark" ? "light" : "dark", true);
      });
    }

    // Follow the system setting only while the user has not made a choice.
    try {
      const media = window.matchMedia("(prefers-color-scheme: dark)");
      const onChange = function (event) {
        let stored = null;
        try {
          stored = window.localStorage.getItem(THEME_KEY);
        } catch (err) {}
        if (!stored) applyTheme(event.matches ? "dark" : "light", false);
      };
      if (media.addEventListener) media.addEventListener("change", onChange);
      else if (media.addListener) media.addListener(onChange);
    } catch (err) {}
  }

  // ---------------------------------------------------------------- data
  function currentItem() {
    return state.session.items[state.session.index];
  }

  function freshCard() {
    return { revealed: false, typed: "", choice: null, checked: false, feedback: null, showHint: false };
  }

  function expectedOf(item) {
    if (!item) return "";
    if (item.type === "choice") return item.options[item.answer];
    if (item.answers && item.answers.length) return item.answers[0];
    return "";
  }

  // ---------------------------------------------------------------- chrome
  function renderChrome() {
    const stats = core.computeStats(ITEMS, state.progress);
    document.querySelectorAll(".tab").forEach(function (tab) {
      tab.classList.toggle("is-active", tab.dataset.nav === state.view);
    });
    els.streak.textContent = stats.streak > 0 ? stats.streak + "-day streak" : "no streak yet";
    els.footLeft.textContent = state.canStore
      ? "Progress is stored in this browser."
      : "Storage blocked — progress will not persist.";
    if (state.view === "solve" && (PROBLEMS.length || PRACTICE.length)) {
      const solved = Object.keys(state.progress.solved || {}).length;
      els.footRight.textContent = totalProblems() + " problems · " + solved + " solved";
    } else {
      els.footRight.textContent = ITEMS.length
        ? ITEMS.length + " items · " + (stats.due + stats.fresh) + " waiting"
        : "no data";
    }
  }

  // ---------------------------------------------------------------- home
  function homeHtml() {
    const stats = core.computeStats(ITEMS, state.progress);
    const rows = core.conceptRows(ITEMS, state.progress);
    const settings = state.progress.settings;
    const goal = stats.goal || 20;
    const goalPct = Math.min(100, Math.round((stats.todayReviewed / goal) * 100));

    const conceptOptions = ['<option value="">All concepts</option>']
      .concat(
        CONCEPTS.map(function (concept) {
          const selected = settings.concept === concept ? " selected" : "";
          return '<option value="' + esc(concept) + '"' + selected + ">" + esc(concept) + "</option>";
        })
      )
      .join("");

    const lengthOptions = [10, 20, 30, 50]
      .map(function (n) {
        return '<option value="' + n + '"' + (settings.limit === n ? " selected" : "") + ">" + n + " items</option>";
      })
      .join("");

    const goalOptions = [10, 20, 30, 50]
      .map(function (n) {
        return '<option value="' + n + '"' + (settings.goal === n ? " selected" : "") + ">" + n + " reviews</option>";
      })
      .join("");

    const conceptRows = rows
      .map(function (row) {
        const mastered = row.total ? Math.round((row.mastered / row.total) * 100) : 0;
        return (
          '<button class="concept-row" data-action="concept-start" data-concept="' +
          esc(row.concept) +
          '">' +
          '<span class="concept-row__name">' + esc(row.concept) + "</span>" +
          '<span class="concept-row__due">' + row.due + " left</span>" +
          '<span class="meter"><span class="meter__fill" style="width:' + mastered + '%"></span></span>' +
          '<span class="concept-row__pct">' + mastered + "%</span>" +
          "</button>"
        );
      })
      .join("");

    return (
      '<section class="row hero">' +
      "<div>" +
      '<p class="eyebrow">Active recall · spaced repetition</p>' +
      "<h1>Remember the pattern,<br>not the problem.</h1>" +
      '<p class="lede">' +
      (stats.due + stats.fresh) +
      " items are waiting. Review what is due, then learn something new. " +
      "Ten focused minutes beat an hour of re-reading.</p>" +
      "</div>" +
      '<div class="hero__side">' +
      '<span class="goal-num">' + stats.todayReviewed + "<span>/" + goal + "</span></span>" +
      '<span class="meta">reviewed today</span>' +
      "</div>" +
      "</section>" +
      '<div class="progress-row"><span class="progress__fill" style="width:' + goalPct + '%"></span></div>' +
      '<section class="row controls">' +
      '<label class="field"><span class="label">Concept</span>' +
      '<select id="concept">' + conceptOptions + "</select></label>" +
      '<label class="field"><span class="label">Session length</span>' +
      '<select id="length">' + lengthOptions + "</select></label>" +
      '<label class="field"><span class="label">Daily goal</span>' +
      '<select id="goal">' + goalOptions + "</select></label>" +
      '<button class="btn btn--solid" data-action="start">Start session</button>' +
      "</section>" +
      '<section class="metrics">' +
      metric(stats.due + stats.fresh, "to review") +
      metric(stats.fresh, "new") +
      metric(stats.learning + stats.young, "in progress") +
      metric(stats.mature, "mastered") +
      "</section>" +
      '<section class="row section-head"><h2>By concept</h2><span class="meta">click a row to start</span></section>' +
      conceptRows +
      '<section class="row actions">' +
      '<button class="btn btn--text" data-action="export">Export progress</button>' +
      '<label class="btn btn--text">Import progress<input type="file" id="importFile" accept="application/json" hidden></label>' +
      '<button class="btn btn--text" data-action="reset">Reset progress</button>' +
      (settings.concept
        ? '<button class="btn btn--text" data-action="clear-concept">Clear filter</button>'
        : "") +
      "</section>" +
      howItWorksHtml()
    );
  }

  function metric(value, label) {
    return '<div class="metric"><span class="metric__num">' + value + '</span><span class="meta">' + label + "</span></div>";
  }

  function howItWorksHtml() {
    return (
      '<details class="cheat">' +
      '<summary><span>How this works</span><span class="meta">30s read</span></summary>' +
      '<div class="cheat__body">' +
      '<p class="cheat__note">Four drill types: recall (answer from memory), ' +
      "multiple choice (spot the right rule), fill the blank (write the template line), " +
      "and predict output (read code precisely).</p>" +
      '<p class="cheat__note">After each item you grade yourself or the app grades you. ' +
      "Grades feed a spaced-repetition schedule: again comes back today, good comes back in days, " +
      "easy in weeks. Low grades shrink the interval, high grades stretch it.</p>" +
      '<p class="cheat__note">The Solve tab has full problems: statement and code on the left, ' +
      "a solution toggle with variants, and a sheet for your own code on the right.</p>" +
      '<p class="cheat__note">Keys: space = primary action, 1-4 = grade or option, escape = home. ' +
      "In the sheet, Tab inserts four spaces and Enter keeps the current indentation.</p>" +
      "</div></details>"
    );
  }

  // ---------------------------------------------------------------- session
  function startSession(options) {
    const opts = options || {};
    const settings = state.progress.settings;
    const items = core.buildSession(ITEMS, state.progress, {
      concept: opts.concept !== undefined ? opts.concept : settings.concept,
      limit: opts.limit || settings.limit,
    });
    state.session = { items: items, index: 0, done: 0, correct: 0 };
    state.card = freshCard();
    state.view = "session";
    render();
    window.scrollTo(0, 0);
  }

  function startAhead() {
    const settings = state.progress.settings;
    const pool = settings.concept
      ? ITEMS.filter(function (item) { return item.concept === settings.concept; })
      : ITEMS;
    const sorted = pool.slice().sort(function (a, b) {
      const da = state.progress.items[a.id] ? state.progress.items[a.id].due : "9999-99-99";
      const db = state.progress.items[b.id] ? state.progress.items[b.id].due : "9999-99-99";
      if (da === db) return a.id < b.id ? -1 : 1;
      return da < db ? -1 : 1;
    });
    state.session = { items: sorted.slice(0, settings.limit), index: 0, done: 0, correct: 0 };
    state.card = freshCard();
    state.view = "session";
    render();
    window.scrollTo(0, 0);
  }

  function sessionHtml() {
    const session = state.session;
    if (!session || !session.items.length) {
      const next = core.nextDueDate(ITEMS, state.progress);
      return (
        '<section class="row hero empty">' +
        "<div>" +
        '<p class="eyebrow">Nothing due</p>' +
        "<h1>All caught up.</h1>" +
        '<p class="lede">' +
        (next ? "Next review: " + esc(next) + ". " : "") +
        "Spacing works better when you wait, but you can study ahead if you want.</p>" +
        "</div></section>" +
        '<section class="row actions">' +
        '<button class="btn btn--solid" data-action="ahead">Study ahead</button>' +
        '<button class="btn" data-action="home">Back home</button>' +
        "</section>"
      );
    }

    if (session.index >= session.items.length) return summaryHtml();

    const item = currentItem();
    const card = state.card;
    const pct = Math.round(((session.index + 1) / session.items.length) * 100);
    const question =
      item.type === "recall" ? item.front : item.type === "choice" ? item.question : item.prompt;

    let out =
      '<section class="row session-head">' +
      '<div class="session-head__left">' +
      '<span class="label">Session</span>' +
      '<span class="mono">' + (session.index + 1) + " / " + session.items.length + "</span>" +
      "</div>" +
      '<div class="session-head__right">' +
      '<span class="badge">' + esc(TYPE_LABEL[item.type] || item.type) + "</span>" +
      '<span class="badge">' + esc(item.concept) + "</span>" +
      "</div></section>" +
      '<div class="progress-row"><span class="progress__fill" style="width:' + pct + '%"></span></div>' +
      '<section class="row question"><div>' +
      '<p class="eyebrow">Question</p>' +
      '<h2 class="q">' + richText(question) + "</h2>" +
      "</div></section>";

    if (item.type === "recall") {
      if (!card.revealed) {
        out +=
          '<section class="row answer">' +
          '<div class="answer__body">' +
          '<p class="eyebrow">Answer</p>' +
          '<p class="meta">Hidden. Recall it fully before revealing.</p>' +
          (item.hint
            ? '<button class="btn btn--text hint-btn" data-action="hint">' +
              (card.showHint ? "Hide hint" : "Show hint") +
              "</button>"
            : "") +
          (card.showHint && item.hint ? '<p class="hint">' + richText(item.hint) + "</p>" : "") +
          "</div>" +
          '<button class="btn btn--solid" data-action="reveal" data-primary>Show answer <kbd>space</kbd></button>' +
          "</section>";
      } else {
        out +=
          '<section class="row answer">' +
          '<div class="answer__body">' +
          '<p class="eyebrow">Answer</p>' +
          '<p class="answer-text">' + richText(item.back) + "</p>" +
          (card.showHint && item.hint ? '<p class="hint">' + richText(item.hint) + "</p>" : "") +
          "</div></section>";
        if (!card.feedback) out += gradesHtml();
      }
    } else if (item.type === "choice") {
      out += optionsHtml(item, card);
    } else if (item.type === "code") {
      out +=
        '<p class="eyebrow code-label">Snippet</p>' +
        codeBlock(item.code) +
        (card.feedback ? "" : typedInputHtml(item, card, "type the missing line"));
    } else if (item.type === "trace") {
      out += item.setup ? codeBlock(item.setup, true) : "";
      out += '<pre class="code-block"><span class="prompt-mark">&gt;</span> ' + highlightPython(item.expr) + "</pre>";
      if (!card.feedback) out += typedInputHtml(item, card, "e.g. 4 or [10, 20]");
    }

    if (card.feedback) out += feedbackHtml(item, card.feedback);
    return out;
  }

  function gradesHtml() {
    return (
      '<section class="grades">' +
      gradeButton(0, "Again") +
      gradeButton(1, "Hard") +
      gradeButton(2, "Good") +
      gradeButton(3, "Easy") +
      "</section>"
    );
  }

  function gradeButton(grade, label) {
    return (
      '<button class="grade" data-action="grade" data-grade="' + grade + '">' +
      '<span class="grade__key">' + (grade + 1) + "</span>" + label +
      "</button>"
    );
  }

  function optionsHtml(item, card) {
    const buttons = item.options.map(function (option, index) {
      let cls = "option";
      let mark = "";
      if (card.feedback) {
        if (index === item.answer) {
          cls += " is-right";
          mark = "correct";
        } else if (index === card.choice) {
          cls += " is-wrong";
          mark = "wrong";
        }
      }
      return (
        '<button class="' + cls + '" data-action="option" data-index="' + index + '"' +
        (card.feedback ? " disabled" : "") + ">" +
        '<span class="option__key">' + (LETTERS[index] || index + 1) + "</span>" +
        '<span class="option__text">' + richText(option) + "</span>" +
        '<span class="option__mark">' + mark + "</span>" +
        "</button>"
      );
    });
    return '<section class="options">' + buttons.join("") + "</section>";
  }

  function typedInputHtml(item, card, placeholder) {
    return (
      '<section class="row answer">' +
      '<div class="answer__body">' +
      '<p class="eyebrow">Your answer</p>' +
      '<div class="inputline">' +
      '<input id="typed" type="text" value="' + esc(card.typed) + '" placeholder="' + esc(placeholder) +
      '" autocomplete="off" spellcheck="false" data-autofocus>' +
      '<button class="btn btn--solid" data-action="check">Check <kbd>enter</kbd></button>' +
      "</div>" +
      '<button class="btn btn--text hint-btn" data-action="reveal">Show answer</button>' +
      "</div></section>"
    );
  }

  function feedbackHtml(item, feedback) {
    if (feedback.pending) {
      return (
        '<section class="row feedback feedback--bad">' +
        '<div class="feedback__body">' +
        '<p class="feedback__title">Not quite</p>' +
        (feedback.given
          ? '<p class="feedback__text">You wrote: <code>' + esc(feedback.given) + "</code></p>"
          : "") +
        '<p class="feedback__text">Expected: <code>' + esc(feedback.expected) + "</code></p>" +
        (item.explain ? '<p class="feedback__text">' + richText(item.explain) + "</p>" : "") +
        "</div></section>" +
        '<section class="grades grades--two">' +
        '<button class="grade" data-action="grade" data-grade="0"><span class="grade__key">1</span>I was wrong</button>' +
        '<button class="grade" data-action="grade" data-grade="2"><span class="grade__key">2</span>My answer was equivalent</button>' +
        "</section>"
      );
    }

    const good = Boolean(feedback.correct);
    return (
      '<section class="row feedback ' + (good ? "feedback--good" : "feedback--bad") + '">' +
      '<div class="feedback__body">' +
      '<p class="feedback__title">' + (good ? "Correct" : "Not quite") + "</p>" +
      (!good && item.type !== "recall"
        ? '<p class="feedback__text">Answer: <code>' + esc(expectedOf(item)) + "</code></p>"
        : "") +
      (item.explain ? '<p class="feedback__text">' + richText(item.explain) + "</p>" : "") +
      "</div>" +
      '<button class="btn btn--solid" data-action="next" data-primary>Next <kbd>space</kbd></button>' +
      "</section>"
    );
  }

  function summaryHtml() {
    const session = state.session;
    const stats = core.computeStats(ITEMS, state.progress);
    const accuracy = session.done ? Math.round((session.correct / session.done) * 100) : 0;
    const next = core.nextDueDate(ITEMS, state.progress);
    return (
      '<section class="row hero summary">' +
      "<div>" +
      '<p class="eyebrow">Session complete</p>' +
      "<h1>" + session.done + " reviewed</h1>" +
      '<p class="lede">' + session.correct + " correct · " + accuracy + "% accuracy · " +
      stats.streak + "-day streak</p>" +
      "</div></section>" +
      '<section class="metrics">' +
      metric(session.done, "reviewed") +
      metric(session.correct, "correct") +
      metric(accuracy + "%", "accuracy") +
      metric(next || "—", "next review") +
      "</section>" +
      '<section class="row actions">' +
      '<button class="btn btn--solid" data-action="start">Another session</button>' +
      '<button class="btn" data-action="home">Back home</button>' +
      "</section>"
    );
  }

  // ---------------------------------------------------------------- solve
  function activeProblems() {
    return state.solve.source === "practice" ? PRACTICE : PROBLEMS;
  }

  function totalProblems() {
    return PROBLEMS.length + PRACTICE.length;
  }

  function currentProblem() {
    const list = activeProblems();
    return list[Math.min(state.solve.index, list.length - 1)] || null;
  }

  function groupedOptions(list, selectedIndex) {
    const groups = new Map();
    list.forEach(function (item, index) {
      if (!groups.has(item.concept)) groups.set(item.concept, []);
      groups.get(item.concept).push({ item: item, index: index });
    });
    return Array.from(groups.entries())
      .map(function (entry) {
        const options = entry[1]
          .map(function (row) {
            return (
              '<option value="' + row.index + '"' +
              (row.index === selectedIndex ? " selected" : "") +
              ">" + esc(row.item.title) + "</option>"
            );
          })
          .join("");
        return '<optgroup label="' + esc(entry[0]) + '">' + options + "</optgroup>";
      })
      .join("");
  }

  function sourceTabsHtml() {
    const curated = state.solve.source !== "practice";
    return (
      '<section class="row solve-source">' +
      '<div class="source-tabs">' +
      '<button class="source-tab' + (curated ? " is-active" : "") + '"' +
      ' data-action="source" data-source="curated"' +
      (PROBLEMS.length ? "" : " disabled") + '>Curated <span class="meta">' +
      PROBLEMS.length + "</span></button>" +
      '<button class="source-tab' + (!curated ? " is-active" : "") + '"' +
      ' data-action="source" data-source="practice"' +
      (PRACTICE.length ? "" : " disabled") + '>practice/ <span class="meta">' +
      PRACTICE.length + "</span></button>" +
      "</div>" +
      '<span class="meta">' +
      (curated ? "solve_bank.py · curated with solution variants" : "practice/*.py · read from your files") +
      "</span></section>"
    );
  }

  function loadNotes() {
    try {
      const raw = window.localStorage.getItem(NOTES_KEY);
      const parsed = raw ? JSON.parse(raw) : {};
      return parsed && typeof parsed === "object" ? parsed : {};
    } catch (err) {
      return {};
    }
  }

  let notesTimer = null;

  function setSheetStatus(text) {
    const el = document.getElementById("sheetStatus");
    if (el) el.textContent = text;
  }

  function persistNotes() {
    clearTimeout(notesTimer);
    try {
      window.localStorage.setItem(NOTES_KEY, JSON.stringify(state.notes));
    } catch (err) {
      /* the sheet still works for this tab */
    }
    setSheetStatus("saved");
  }

  function schedulePersistNotes() {
    clearTimeout(notesTimer);
    notesTimer = setTimeout(persistNotes, 300);
  }

  function updateGutter() {
    const sheet = document.getElementById("sheet");
    const gutter = document.getElementById("gutter");
    if (!sheet || !gutter) return;
    const count = sheet.value.split("\n").length;
    const lines = [];
    for (let i = 1; i <= Math.max(count, 1); i += 1) lines.push(i);
    gutter.textContent = lines.join("\n");
    gutter.scrollTop = sheet.scrollTop;
  }

  function updateSheetHighlight() {
    const sheet = document.getElementById("sheet");
    const pre = document.getElementById("sheetHighlight");
    if (!sheet || !pre) return;
    pre.innerHTML = highlightPython(sheet.value) + "\n";
    pre.scrollTop = sheet.scrollTop;
    pre.scrollLeft = sheet.scrollLeft;
  }

  function recordSheetValue(value) {
    const problem = currentProblem();
    if (!problem) return;
    state.notes[problem.id] = value;
    setSheetStatus("saving...");
    schedulePersistNotes();
    updateGutter();
    updateSheetHighlight();
  }

  function goToProblem(index) {
    const list = activeProblems();
    if (!list.length) return;
    persistNotes();
    const next = Math.max(0, Math.min(list.length - 1, index));
    state.solve.index = next;
    state.solve.solutionOpen = false;
    state.solve.variant = 0;
    try {
      window.localStorage.setItem(PROBLEM_KEY, state.solve.source + ":" + list[next].id);
    } catch (err) {}
    render();
  }

  function toggleSolved() {
    const problem = currentProblem();
    if (!problem) return;
    if (!state.progress.solved) state.progress.solved = {};
    if (state.progress.solved[problem.id]) {
      delete state.progress.solved[problem.id];
    } else {
      state.progress.solved[problem.id] = core.todayISO();
    }
    saveProgress();
    const solvedNow = Boolean(state.progress.solved[problem.id]);
    const button = document.querySelector('[data-action="toggle-solved"]');
    if (button) {
      button.textContent = solvedNow ? "Solved" : "Mark solved";
      button.classList.toggle("is-on", solvedNow);
    }
    const solvedTotal = Object.keys(state.progress.solved).length;
    const count = document.getElementById("solvedCount");
    if (count) {
      count.textContent = solvedTotal + " of " + totalProblems() + " solved";
    }
    const footer = document.getElementById("footRight");
    if (footer) {
      footer.textContent = totalProblems() + " problems · " + solvedTotal + " solved";
    }
  }

  function copySheet() {
    const sheet = document.getElementById("sheet");
    if (!sheet) return;
    const text = sheet.value;
    function done() { setSheetStatus("copied"); }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { setSheetStatus("copy failed"); });
    } else {
      sheet.select();
      try {
        document.execCommand("copy");
        done();
      } catch (err) {
        setSheetStatus("copy failed");
      }
    }
    sheet.focus({ preventScroll: true });
  }

  function resetSheet() {
    const problem = currentProblem();
    if (!problem) return;
    if (!window.confirm("Clear your sheet for this problem?")) return;
    state.notes[problem.id] = "";
    persistNotes();
    const sheet = document.getElementById("sheet");
    if (sheet) {
      sheet.value = "";
      sheet.focus({ preventScroll: true });
    }
    updateGutter();
    updateSheetHighlight();
    setSheetStatus("cleared");
  }

  function setRunButton(label, disabled) {
    const button = document.querySelector('[data-action="run-sheet"]');
    if (!button) return;
    button.textContent = label;
    if (disabled) button.setAttribute("disabled", "disabled");
    else button.removeAttribute("disabled");
  }

  function showRunResults(data) {
    const panel = document.getElementById("runPanel");
    if (!panel) return;
    panel.hidden = false;
    if (data.error) {
      panel.innerHTML = '<div class="run-summary run-summary--bad">' + esc(data.error) + "</div>";
      return;
    }
    const results = data.results || [];
    const total = data.total || results.length;
    const passed = data.passed || 0;
    let html = '<div class="run-summary">' + passed + " / " + total + " passed</div>";
    results.forEach(function (result) {
      const detail = result.error
        ? '<span class="run-detail">' + esc(result.error) + "</span>"
        : result.passed
          ? ""
          : '<span class="run-detail">expected ' + esc(result.expected) + " \u00b7 got " + esc(result.got) + "</span>";
      html += '<div class="run-result ' + (result.passed ? "is-pass" : "is-fail") + '">' +
        '<span class="run-result__mark">' + (result.passed ? "[v]" : "[x]") + "</span> " +
        esc(result.label) + detail + "</div>";
    });
    panel.innerHTML = html;
  }

  function runSheet() {
    const problem = currentProblem();
    if (!problem || !problem.runnable) return;
    const problemId = problem.id;
    persistNotes();
    const sheet = document.getElementById("sheet");
    const code = sheet ? sheet.value : "";
    const panel = document.getElementById("runPanel");
    if (panel) {
      panel.hidden = false;
      panel.innerHTML = '<div class="run-summary">Running...</div>';
    }
    setRunButton("Running...", true);
    fetch("/api/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ problem_id: problemId, code: code }),
    })
      .then(function (response) {
        return response.json().then(function (body) {
          if (!response.ok) throw new Error(body.error || "HTTP " + response.status);
          return body;
        });
      })
      .then(function (data) {
        const current = currentProblem();
        if (!current || current.id !== problemId) return;
        showRunResults(data);
        setRunButton("Run tests", false);
      })
      .catch(function (error) {
        const current = currentProblem();
        if (!current || current.id !== problemId) return;
        const target = document.getElementById("runPanel");
        if (target) {
          target.hidden = false;
          target.innerHTML = '<div class="run-summary run-summary--bad">' + esc(error.message) + "</div>";
        }
        setRunButton("Run tests", false);
      });
  }

  function handleSheetKey(event) {
    if (!event.target || event.target.id !== "sheet") return;
    const sheet = event.target;
    if (event.key === "Tab") {
      event.preventDefault();
      const start = sheet.selectionStart;
      const end = sheet.selectionEnd;
      sheet.value = sheet.value.slice(0, start) + "    " + sheet.value.slice(end);
      sheet.selectionStart = sheet.selectionEnd = start + 4;
      recordSheetValue(sheet.value);
      return;
    }
    if (event.key === "Enter") {
      const start = sheet.selectionStart;
      const before = sheet.value.slice(0, start);
      const line = before.slice(before.lastIndexOf("\n") + 1);
      const indent = line.match(/^[ \t]*/)[0];
      if (!indent) return;
      event.preventDefault();
      const insert = "\n" + indent;
      sheet.value = sheet.value.slice(0, start) + insert + sheet.value.slice(sheet.selectionEnd);
      sheet.selectionStart = sheet.selectionEnd = start + insert.length;
      recordSheetValue(sheet.value);
    }
  }

  function exampleHtml(example, index) {
    return (
      '<div class="example">' +
      '<p class="eyebrow">Example ' + (index + 1) + "</p>" +
      '<p class="example-line"><span class="label">Input</span><code>' + esc(example.input) + "</code></p>" +
      '<p class="example-line"><span class="label">Output</span><code>' + esc(example.output) + "</code></p>" +
      (example.why
        ? '<p class="example-line"><span class="label">Why</span><span>' + inlineMd(example.why) + "</span></p>"
        : "") +
      "</div>"
    );
  }

  function solutionHtml(problem) {
    const activeIndex = Math.min(state.solve.variant, problem.variants.length - 1);
    const active = problem.variants[activeIndex];
    const tabs = problem.variants
      .map(function (variant, index) {
        return (
          '<button class="variant' + (index === activeIndex ? " is-active" : "") + '"' +
          ' data-action="variant" data-index="' + index + '" role="tab"' +
          ' aria-selected="' + (index === activeIndex ? "true" : "false") + '">' +
          esc(variant.name) + "</button>"
        );
      })
      .join("");

    return (
      '<div class="variants" role="tablist">' + tabs + "</div>" +
      '<div class="solution-body">' +
      '<div class="solution-meta">' +
      '<p class="eyebrow">Variant ' + (activeIndex + 1) + " of " + problem.variants.length + "</p>" +
      '<p class="solution-complexity">' + esc(active.complexity) + "</p>" +
      '<p class="solution-note">' + inlineMd(active.note) + "</p>" +
      "</div>" +
      codeBlock(active.code) +
      "</div>"
    );
  }

  function solveHtml() {
    const list = activeProblems();
    const tabs = sourceTabsHtml();

    if (!list.length) {
      return (
        tabs +
        '<section class="row hero empty"><div>' +
        '<p class="eyebrow">No problems</p>' +
        "<h1>This source is empty.</h1>" +
        '<p class="lede">Add curated problems to <code>learning/solve_bank.py</code> or problems to <code>practice/</code>.</p>' +
        "</div></section>"
      );
    }

    const index = Math.min(state.solve.index, list.length - 1);
    state.solve.index = index;
    const problem = list[index];
    const note = state.notes[problem.id] || "";
    const solved = state.progress.solved || {};
    const isSolved = Boolean(solved[problem.id]);
    const solvedCount = Object.keys(solved).length;
    const options = groupedOptions(list, index);

    const examples = (problem.examples || []).length
      ? (problem.examples || [])
          .map(function (example, position) { return exampleHtml(example, position); })
          .join("")
      : '<p class="meta">No examples listed in the file.</p>';

    const constraints = (problem.constraints || []).length
      ? '<ul class="md-list">' +
        (problem.constraints || [])
          .map(function (line) { return "<li>" + inlineMd(line) + "</li>"; })
          .join("") +
        "</ul>"
      : '<p class="meta">No constraints listed in the file.</p>';

    const prevDisabled = index === 0 ? " disabled" : "";
    const nextDisabled = index === list.length - 1 ? " disabled" : "";
    const functionHint = problem.function
      ? " · tests call <code>" + esc(problem.function) + "</code>"
      : "";
    const sourceLine = problem.source
      ? '<p class="meta">' + esc(problem.source) +
        (problem.leetcode ? " · LeetCode " + esc(problem.leetcode) : "") +
        functionHint + "</p>"
      : "";
    const leetcodeBadge = problem.leetcode
      ? '<span class="badge">LC ' + esc(problem.leetcode) + "</span>"
      : "";

    return (
      tabs +
      '<section class="row solve-head">' +
      '<div class="solve-head__left">' +
      '<span class="label">Solve</span>' +
      '<span class="mono">' + (index + 1) + " / " + list.length + "</span>" +
      '<span class="badge">' + esc(problem.difficulty) + "</span>" +
      '<span class="badge">' + esc(problem.concept) + "</span>" +
      leetcodeBadge +
      "</div>" +
      '<div class="solve-head__right">' +
      '<button class="btn btn--text" data-action="problem-prev"' + prevDisabled + ">Prev</button>" +
      '<select id="problemSelect" aria-label="Problem">' + options + "</select>" +
      '<button class="btn btn--text" data-action="problem-next"' + nextDisabled + ">Next</button>" +
      "</div></section>" +
      '<div class="solve-split">' +
      '<section class="solve-pane solve-pane--left">' +
      '<div class="problem-head">' +
      '<p class="eyebrow">Problem</p>' +
      '<h1 class="problem-title">' + esc(problem.title) + "</h1>" +
      sourceLine +
      '<p class="meta" id="solvedCount">' + solvedCount + " of " + totalProblems() + " solved</p>" +
      "</div>" +
      '<div class="solution-controls">' +
      '<button class="btn' + (state.solve.solutionOpen ? " is-on" : "") + '"' +
      ' data-action="toggle-solution" aria-expanded="' +
      (state.solve.solutionOpen ? "true" : "false") + '">' +
      (state.solve.solutionOpen ? "Hide solution" : "Show solution") +
      "</button>" +
      '<button class="btn btn--text' + (isSolved ? " is-on" : "") + '" data-action="toggle-solved">' +
      (isSolved ? "Solved" : "Mark solved") +
      "</button>" +
      "</div>" +
      '<div class="problem-block">' + markdown(problem.statement) + "</div>" +
      '<div class="problem-block">' + examples + "</div>" +
      '<div class="problem-block"><p class="eyebrow">Constraints</p>' +
      constraints + "</div>" +
      (state.solve.solutionOpen ? solutionHtml(problem) : "") +
      "</section>" +
      '<section class="solve-pane solve-pane--right">' +
      '<div class="sheet-bar">' +
      '<span class="label">Your sheet</span>' +
      '<span class="meta" id="sheetStatus">saved</span>' +
      '<div class="sheet-actions">' +
      (problem.runnable
        ? '<button class="btn btn--text" data-action="run-sheet">Run tests</button>'
        : "") +
      '<button class="btn btn--text" data-action="sheet-copy">Copy</button>' +
      '<button class="btn btn--text" data-action="sheet-reset">Reset</button>' +
      "</div></div>" +
      '<div class="sheet-body">' +
      '<pre class="sheet-gutter" id="gutter" aria-hidden="true">1</pre>' +
      '<div class="sheet-code">' +
      '<pre class="sheet-highlight" id="sheetHighlight" aria-hidden="true"></pre>' +
      '<textarea id="sheet" class="sheet-input" spellcheck="false" autocomplete="off"' +
      ' aria-label="Your solution sheet" placeholder="# write your solution here">' +
      esc(note) +
      "</textarea>" +
      "</div></div>" +
      '<div class="run-panel" id="runPanel" hidden></div>' +
      "</section></div>"
    );
  }

  function rerenderSolve(keepScroll) {
    const pane = document.querySelector(".solve-pane--left");
    const top = pane ? pane.scrollTop : 0;
    render();
    if (keepScroll) {
      const next = document.querySelector(".solve-pane--left");
      if (next) next.scrollTop = top;
    }
  }

  function afterSolveRender() {
    updateGutter();
    updateSheetHighlight();
    const sheet = document.getElementById("sheet");
    if (!sheet) return;
    sheet.addEventListener("scroll", function () {
      const gutter = document.getElementById("gutter");
      if (gutter) gutter.scrollTop = sheet.scrollTop;
      const pre = document.getElementById("sheetHighlight");
      if (pre) {
        pre.scrollTop = sheet.scrollTop;
        pre.scrollLeft = sheet.scrollLeft;
      }
    });
  }

  // ---------------------------------------------------------------- graph
  let graphHoverId = null;

  function graphProgress() {
    const rows = core.conceptRows(ITEMS, state.progress);
    const map = {};
    let reviewed = 0;
    let total = 0;
    let mastered = 0;
    rows.forEach(function (row) {
      const reviewedCount = row.total - row.fresh;
      map[row.concept] = {
        total: row.total,
        reviewed: reviewedCount,
        mastered: row.mastered,
        due: row.due,
      };
      reviewed += reviewedCount;
      total += row.total;
      mastered += row.mastered;
    });
    return { map: map, reviewed: reviewed, total: total, mastered: mastered };
  }

  function fitText(ctx, text, maxWidth) {
    if (ctx.measureText(text).width <= maxWidth) return text;
    let result = String(text);
    while (result.length > 1 && ctx.measureText(result + "…").width > maxWidth) {
      result = result.slice(0, -1);
    }
    return result + "…";
  }

  function graphNodeAt(event) {
    const canvas = document.getElementById("graph");
    if (!canvas) return null;
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    return (
      GRAPH.nodes.find(function (node) {
        return (
          node.x != null &&
          x >= node.x &&
          x <= node.x + node.w &&
          y >= node.y &&
          y <= node.y + node.h
        );
      }) || null
    );
  }

  function setGraphInfo(node) {
    const info = document.getElementById("graphInfo");
    if (!info) return;
    if (!node) {
      info.textContent = "Hover a node for details. Click a node to drill it.";
      return;
    }
    const stats = graphProgress().map[node.concept] || { reviewed: 0, total: 0, mastered: 0, due: 0 };
    info.textContent =
      node.concept +
      " — " + stats.reviewed + "/" + stats.total + " reviewed · " +
      stats.mastered + " mastered" + (stats.due ? " · " + stats.due + " due" : "");
  }

  function drawGraph() {
    const canvas = document.getElementById("graph");
    if (!canvas || !GRAPH.nodes.length) return;
    const wrap = canvas.parentElement;
    const root = getComputedStyle(document.documentElement);
    const cssVar = function (name) { return root.getPropertyValue(name).trim(); };
    const bg = cssVar("--bg");
    const fg = cssVar("--fg");
    const muted = cssVar("--muted");
    const line = cssVar("--line");
    const hover = cssVar("--hover");
    const good = cssVar("--good");

    const dpr = window.devicePixelRatio || 1;
    const designWidth = 1000;
    const cssWidth = Math.max(wrap.clientWidth || designWidth, designWidth);
    const padX = 24;
    const padY = 28;
    const gapX = 18;
    const gapY = 30;
    const nodeH = 58;

    const layers = [];
    GRAPH.nodes.forEach(function (node) {
      if (!layers[node.layer]) layers[node.layer] = [];
      layers[node.layer].push(node);
    });
    const maxPerLayer = Math.max.apply(null, layers.map(function (layer) { return layer.length; }));
    const nodeW = Math.min(190, (cssWidth - padX * 2 - gapX * (maxPerLayer - 1)) / maxPerLayer);
    const height = padY * 2 + layers.length * nodeH + (layers.length - 1) * gapY;

    canvas.style.width = Math.round(cssWidth) + "px";
    canvas.style.height = Math.round(height) + "px";
    canvas.width = Math.round(cssWidth * dpr);
    canvas.height = Math.round(height * dpr);

    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, cssWidth, height);

    layers.forEach(function (layer, layerIndex) {
      if (!layer) return;
      const totalWidth = layer.length * nodeW + (layer.length - 1) * gapX;
      const startX = (cssWidth - totalWidth) / 2;
      layer.forEach(function (node, index) {
        node.x = Math.round(startX + index * (nodeW + gapX));
        node.y = Math.round(padY + layerIndex * (nodeH + gapY));
        node.w = nodeW;
        node.h = nodeH;
      });
    });

    const byId = {};
    GRAPH.nodes.forEach(function (node) { byId[node.id] = node; });

    ctx.lineWidth = 1;
    GRAPH.edges.forEach(function (edge) {
      const from = byId[edge[0]];
      const to = byId[edge[1]];
      if (!from || !to) return;
      const highlighted = graphHoverId && (edge[0] === graphHoverId || edge[1] === graphHoverId);
      ctx.strokeStyle = highlighted ? fg : line;
      const sx = from.x + from.w / 2;
      const sy = from.y + from.h;
      const tx = to.x + to.w / 2;
      const ty = to.y;
      const mid = (sy + ty) / 2;
      ctx.beginPath();
      ctx.moveTo(sx + 0.5, sy + 0.5);
      ctx.bezierCurveTo(sx + 0.5, mid, tx + 0.5, mid, tx + 0.5, ty + 0.5);
      ctx.stroke();
    });

    const progress = graphProgress();
    GRAPH.nodes.forEach(function (node) {
      const hovered = node.id === graphHoverId;
      const stats = progress.map[node.concept] || { reviewed: 0, total: 0, mastered: 0, due: 0 };
      const ratio = stats.total ? stats.reviewed / stats.total : 0;

      ctx.fillStyle = hovered ? hover : bg;
      ctx.fillRect(node.x, node.y, node.w, node.h);
      ctx.strokeStyle = hovered ? fg : line;
      ctx.lineWidth = 1;
      ctx.strokeRect(node.x + 0.5, node.y + 0.5, node.w - 1, node.h - 1);

      ctx.fillStyle = fg;
      ctx.font = '12px -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif';
      ctx.textAlign = "left";
      ctx.textBaseline = "top";
      ctx.fillText(fitText(ctx, node.label, node.w - 24), node.x + 12, node.y + 11);

      ctx.fillStyle = muted;
      ctx.font = '10px ui-monospace, SFMono-Regular, Menlo, monospace';
      ctx.textAlign = "right";
      ctx.fillText(stats.reviewed + "/" + stats.total, node.x + node.w - 12, node.y + 31);
      ctx.textAlign = "left";

      const barX = node.x + 12;
      const barY = node.y + node.h - 13;
      const barW = node.w - 24;
      ctx.strokeStyle = line;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(barX + 0.5, barY + 0.5);
      ctx.lineTo(barX + barW + 0.5, barY + 0.5);
      ctx.stroke();
      if (ratio > 0) {
        ctx.strokeStyle = good;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(barX + 0.5, barY + 0.5);
        ctx.lineTo(barX + Math.max(1, Math.round(barW * ratio)) + 0.5, barY + 0.5);
        ctx.stroke();
        ctx.lineWidth = 1;
      }
    });
  }

  function graphHtml() {
    const progress = graphProgress();
    const pct = progress.total ? Math.round((progress.reviewed / progress.total) * 100) : 0;
    return (
      '<section class="row graph-head">' +
      '<div class="solve-head__left">' +
      '<span class="label">Graph</span>' +
      '<span class="mono">' + GRAPH.nodes.length + " concepts</span>" +
      '<span class="badge">' + progress.reviewed + " / " + progress.total + " reviewed</span>" +
      '<span class="badge">' + pct + "%</span>" +
      "</div>" +
      '<span class="meta">bar = reviewed / total</span>' +
      "</section>" +
      '<div class="graph-wrap"><canvas id="graph" role="img" aria-label="Knowledge graph of ' +
      GRAPH.nodes.length + ' concepts with review progress"></canvas></div>' +
      '<div class="row graph-info"><span id="graphInfo">Hover a node for details. Click a node to drill it.</span></div>'
    );
  }

  function afterGraphRender() {
    graphHoverId = null;
    drawGraph();
    setGraphInfo(null);
    const canvas = document.getElementById("graph");
    if (!canvas) return;
    canvas.addEventListener("mousemove", function (event) {
      const node = graphNodeAt(event);
      canvas.style.cursor = node ? "pointer" : "default";
      const id = node ? node.id : null;
      if (id !== graphHoverId) {
        graphHoverId = id;
        drawGraph();
        setGraphInfo(node);
      }
    });
    canvas.addEventListener("mouseleave", function () {
      graphHoverId = null;
      drawGraph();
      setGraphInfo(null);
    });
    canvas.addEventListener("click", function (event) {
      const node = graphNodeAt(event);
      if (!node) return;
      startSession({ concept: node.concept });
      writeHash("session");
    });
  }

  // ---------------------------------------------------------------- cheatsheet


  const GROUP_ORDER = ["Essentials", "Patterns", "Graphs", "DP", "Structures", "Matrix & bits", "Strings", "Meta"];
  let cheatQuery = "";

  function cheatText(section) {
    const parts = [section.group, section.title, section.tag, section.note || ""];
    if (section.code) parts.push(section.code);
    if (section.table) {
      section.table.forEach(function (row) { parts.push(row.join(" ")); });
    }
    return parts.join("\n").toLowerCase();
  }

  function cheatsheetHtml() {
    if (!CHEATS.length) {
      return (
        '<section class="row hero empty"><div>' +
        '<p class="eyebrow">No sections</p>' +
        "<h1>The cheat sheet is empty.</h1>" +
        '<p class="lede">Add sections to <code>learning/study/cheatsheet.json</code>.</p>' +
        "</div></section>"
      );
    }

    const groups = new Map();
    CHEATS.forEach(function (section) {
      if (!groups.has(section.group)) groups.set(section.group, []);
      groups.get(section.group).push(section);
    });
    const order = GROUP_ORDER.concat(
      Array.from(groups.keys()).filter(function (group) {
        return GROUP_ORDER.indexOf(group) === -1;
      })
    );

    let html =
      '<section class="row section-head"><h2>Cheatsheet</h2>' +
      '<span class="meta">write these from memory</span></section>' +
      '<section class="row cheat-search">' +
      '<input id="cheatSearch" type="text" placeholder="Filter sections..." value="' +
      esc(cheatQuery) + '" autocomplete="off" spellcheck="false">' +
      '<span class="meta" id="cheatCount">' + CHEATS.length + " of " + CHEATS.length +
      " sections</span></section>";

    let index = 0;
    order.forEach(function (group) {
      const sections = groups.get(group);
      if (!sections) return;
      html += '<section class="cheat-group" data-group="' + esc(group) + '">' +
        '<p class="cheat-group__title">' + esc(group) +
        ' <span class="meta">' + sections.length + "</span></p>";
      sections.forEach(function (section) {
        const body = section.table ? tableHtml(section.table) : codeBlock(section.code);
        html += '<details class="cheat" data-search="' + esc(cheatText(section)) + '"' +
          (index === 0 ? " open" : "") + ">" +
          '<summary><span>' + esc(section.title) + '</span><span class="meta">' +
          esc(section.tag) + "</span></summary>" +
          '<div class="cheat__body">' +
          (section.note ? '<p class="cheat__note">' + esc(section.note) + "</p>" : "") +
          body +
          "</div></details>";
        index += 1;
      });
      html += "</section>";
    });
    return html;
  }

  function filterCheats() {
    const query = cheatQuery.trim().toLowerCase();
    let visible = 0;
    document.querySelectorAll(".cheat[data-search]").forEach(function (element) {
      const match = !query || element.dataset.search.indexOf(query) !== -1;
      element.hidden = !match;
      if (match) visible += 1;
    });
    document.querySelectorAll(".cheat-group").forEach(function (group) {
      group.hidden = !group.querySelector(".cheat:not([hidden])");
    });
    const count = document.getElementById("cheatCount");
    if (count) count.textContent = visible + " of " + CHEATS.length + " sections";
  }

  function tableHtml(rows) {
    return (
      '<table class="table"><thead><tr><th>Expression</th><th>Result</th><th>Why</th></tr></thead><tbody>' +
      rows
        .map(function (row) {
          return (
            "<tr><td><code>" + esc(row[0]) + "</code></td>" +
            "<td><code>" + esc(row[1]) + "</code></td>" +
            "<td>" + esc(row[2]) + "</td></tr>"
          );
        })
        .join("") +
      "</tbody></table>"
    );
  }

  // ---------------------------------------------------------------- actions
  function revealCurrent() {
    const item = currentItem();
    if (!item || state.card.feedback) return;
    state.card.revealed = true;
    if (item.type === "code" || item.type === "trace") {
      state.card.feedback = { pending: true, expected: expectedOf(item) };
    }
    render();
  }

  function checkTyped() {
    const item = currentItem();
    const typed = state.card.typed;
    if (!typed.trim()) return;
    if (core.matchesAnswer(typed, item.answers)) {
      finish(3, true);
      return;
    }
    state.card.checked = true;
    state.card.feedback = { pending: true, expected: expectedOf(item), given: typed };
    render();
  }

  function finish(grade, correct) {
    const item = currentItem();
    core.recordResult(state.progress, item, grade, core.todayISO());
    state.session.done += 1;
    if (correct) state.session.correct += 1;
    saveProgress();
    state.card.feedback = { done: true, correct: Boolean(correct), grade: grade };
    state.card.checked = true;
    render();
  }

  function nextCard() {
    state.session.index += 1;
    state.card = freshCard();
    render();
    window.scrollTo(0, 0);
  }

  function primary() {
    if (state.view !== "session") return;
    const session = state.session;
    if (!session || !session.items.length) return;
    if (session.index >= session.items.length) {
      startSession();
      return;
    }
    const card = state.card;
    if (card.feedback) {
      if (!card.feedback.pending) nextCard();
      return;
    }
    const item = currentItem();
    if (item.type === "recall" && !card.revealed) {
      revealCurrent();
      return;
    }
    if (item.type === "code" || item.type === "trace") checkTyped();
  }

  function exportProgress() {
    const blob = new Blob([JSON.stringify(state.progress, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "dsa-study-progress.json";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }

  function importProgress(file) {
    const reader = new FileReader();
    reader.onload = function () {
      try {
        const parsed = JSON.parse(String(reader.result));
        state.progress = core.ensureProgress(parsed);
        saveProgress();
        state.session = null;
        state.view = "home";
        render();
      } catch (err) {
        window.alert("That file is not a valid progress export.");
      }
    };
    reader.readAsText(file);
  }

  // ---------------------------------------------------------------- events
  document.addEventListener("click", function (event) {
    const nav = event.target.closest("[data-nav]");
    if (nav) {
      navigate(nav.dataset.nav);
      return;
    }

    const target = event.target.closest("[data-action]");
    if (!target) return;
    const action = target.dataset.action;

    if (action === "start") {
      startSession();
    } else if (action === "ahead") {
      startAhead();
    } else if (action === "home") {
      navigate("home");
    } else if (action === "reveal") {
      revealCurrent();
    } else if (action === "hint") {
      state.card.showHint = !state.card.showHint;
      render();
    } else if (action === "check") {
      checkTyped();
    } else if (action === "next") {
      nextCard();
    } else if (action === "option") {
      if (state.card.checked) return;
      const index = Number(target.dataset.index);
      const item = currentItem();
      state.card.choice = index;
      finish(index === item.answer ? 3 : 0, index === item.answer);
    } else if (action === "grade") {
      const grade = Number(target.dataset.grade);
      finish(grade, grade >= 2);
    } else if (action === "concept-start") {
      state.progress.settings.concept = target.dataset.concept;
      saveProgress();
      startSession({ concept: target.dataset.concept });
    } else if (action === "clear-concept") {
      state.progress.settings.concept = "";
      saveProgress();
      render();
    } else if (action === "source") {
      const source = target.dataset.source;
      if (source !== "curated" && source !== "practice") return;
      if (source === state.solve.source) return;
      state.solve.source = source;
      state.solve.index = 0;
      state.solve.solutionOpen = false;
      state.solve.variant = 0;
      const list = activeProblems();
      if (list.length) {
        try {
          window.localStorage.setItem(PROBLEM_KEY, source + ":" + list[0].id);
        } catch (err) {}
      }
      render();
    } else if (action === "problem-prev") {
      goToProblem(state.solve.index - 1);
    } else if (action === "problem-next") {
      goToProblem(state.solve.index + 1);
    } else if (action === "toggle-solution") {
      state.solve.solutionOpen = !state.solve.solutionOpen;
      render();
      const pane = document.querySelector(".solve-pane--left");
      if (pane) {
        const variants = document.querySelector(".variants");
        pane.scrollTop = state.solve.solutionOpen && variants ? variants.offsetTop - 8 : 0;
      }
    } else if (action === "variant") {
      state.solve.variant = Number(target.dataset.index) || 0;
      rerenderSolve(true);
    } else if (action === "toggle-solved") {
      toggleSolved();
    } else if (action === "run-sheet") {
      runSheet();
    } else if (action === "sheet-copy") {
      copySheet();
    } else if (action === "sheet-reset") {
      resetSheet();
    } else if (action === "export") {
      exportProgress();
    } else if (action === "reset") {
      if (window.confirm("Reset all progress? This cannot be undone.")) {
        state.progress = core.emptyProgress();
        saveProgress();
        state.session = null;
        state.view = "home";
        render();
      }
    }
  });

  document.addEventListener("change", function (event) {
    const target = event.target;
    if (target.id === "concept") {
      state.progress.settings.concept = target.value;
      saveProgress();
    } else if (target.id === "length") {
      state.progress.settings.limit = Number(target.value) || 20;
      saveProgress();
    } else if (target.id === "goal") {
      state.progress.settings.goal = Number(target.value) || 20;
      saveProgress();
    } else if (target.id === "problemSelect") {
      goToProblem(Number(target.value));
    } else if (target.id === "importFile") {
      if (target.files && target.files[0]) importProgress(target.files[0]);
      target.value = "";
    }
  });

  document.addEventListener("input", function (event) {
    if (event.target.id === "typed") {
      state.card.typed = event.target.value;
    } else if (event.target.id === "sheet") {
      recordSheetValue(event.target.value);
    } else if (event.target.id === "cheatSearch") {
      cheatQuery = event.target.value;
      filterCheats();
    }
  });

  document.addEventListener("keydown", handleSheetKey);

  document.addEventListener("keydown", function (event) {
    if (state.view !== "session") return;
    if (event.key === "Escape") {
      navigate("home");
      return;
    }

    const tag = (event.target && event.target.tagName ? event.target.tagName : "").toLowerCase();
    const typing = tag === "input" || tag === "textarea" || tag === "select";

    if (typing) {
      if (event.key === "Enter" && tag === "input") {
        event.preventDefault();
        checkTyped();
      }
      return;
    }

    const isButton = tag === "button";
    if ((event.key === " " || event.key === "Enter") && !isButton) {
      event.preventDefault();
      primary();
      return;
    }

    if (!state.card || state.card.feedback) {
      if (/^[12]$/.test(event.key) && state.card && state.card.feedback && state.card.feedback.pending) {
        finish(Number(event.key) === 1 ? 0 : 2, Number(event.key) === 2);
        return;
      }
      if (/^[1-4]$/.test(event.key) && state.card && state.card.feedback && !state.card.feedback.pending) {
        // after a done grade, numbers do nothing; space moves on
        return;
      }
    }

    if (state.card && !state.card.checked && /^[1-4]$/.test(event.key)) {
      const item = currentItem();
      if (!item) return;
      if (item.type === "recall" && state.card.revealed) {
        finish(Number(event.key) - 1, Number(event.key) >= 3);
      } else if (item.type === "choice") {
        const index = Number(event.key) - 1;
        if (index < item.options.length) {
          state.card.choice = index;
          finish(index === item.answer ? 3 : 0, index === item.answer);
        }
      }
    }
  });

  // ---------------------------------------------------------------- render
  function render() {
    renderChrome();
    document.body.className = state.view === "solve" ? "is-solve" : "";
    els.view.className = state.view === "solve" ? "view--solve" : "";
    if (state.view === "session") {
      els.view.innerHTML = sessionHtml();
    } else if (state.view === "solve") {
      els.view.innerHTML = solveHtml();
      afterSolveRender();
    } else if (state.view === "graph") {
      els.view.innerHTML = graphHtml();
      afterGraphRender();
    } else if (state.view === "cheatsheet") {
      els.view.innerHTML = cheatsheetHtml();
      filterCheats();
    } else {
      els.view.innerHTML = homeHtml();
    }

    if (state.view !== state.lastView) {
      state.lastView = state.view;
      window.scrollTo(0, 0);
    }

    const input = els.view.querySelector("#typed");
    if (input) {
      input.focus({ preventScroll: true });
      const end = input.value.length;
      try {
        input.setSelectionRange(end, end);
      } catch (err) {
        /* some browsers disallow it on certain inputs */
      }
    } else {
      const primaryButton = els.view.querySelector("[data-primary]");
      if (primaryButton && document.activeElement !== primaryButton) {
        primaryButton.focus({ preventScroll: true });
      }
    }
  }

  function writeHash(view) {
    try {
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, "", "#" + view);
      }
    } catch (err) {
      /* file:// in some browsers forbids replaceState; navigation still works */
    }
  }

  function navigate(view) {
    if (!state.loaded) return;
    if (view === "session") {
      if (!state.session || state.session.index >= state.session.items.length) {
        startSession();
      } else {
        state.view = "session";
        render();
      }
    } else {
      state.view = view;
      if (view === "home") state.session = null;
      render();
    }
    writeHash(view);
  }

  window.addEventListener("hashchange", function () {
    const hash = (window.location.hash || "").replace("#", "");
    if (hash === "session") navigate("session");
    else if (hash === "solve") navigate("solve");
    else if (hash === "graph") navigate("graph");
    else if (hash === "cheatsheet") navigate("cheatsheet");
    else navigate("home");
  });

  // ---------------------------------------------------------------- boot
  function loadContent() {
    return fetch("/api/content", { cache: "no-store" }).then(function (response) {
      return response
        .json()
        .catch(function () { return {}; })
        .then(function (body) {
          if (!response.ok) {
            const error = new Error(body.error || "HTTP " + response.status);
            error.problems = body.problems || [];
            throw error;
          }
          return body;
        });
    });
  }

  function showLoading() {
    state.view = "home";
    renderChrome();
    document.body.className = "";
    els.view.className = "";
    els.view.innerHTML =
      '<section class="row hero empty"><div>' +
      '<p class="eyebrow">Loading</p>' +
      "<h1>Reading the content files.</h1>" +
      '<p class="lede">Drills, problems and the graph come from the local content server. ' +
      "No content is bundled in the app.</p>" +
      "</div></section>";
  }

  function showLoadError(error) {
    renderChrome();
    document.body.className = "";
    els.view.className = "";
    const details = error && error.problems && error.problems.length
      ? '<pre class="code-block">' + esc(error.problems.join("\n")) + "</pre>"
      : "";
    els.view.innerHTML =
      '<section class="row hero empty"><div>' +
      '<p class="eyebrow">Content unavailable</p>' +
      "<h1>Start the content server.</h1>" +
      '<p class="lede">The app reads <code>/api/content</code> from the local server. ' +
      "Opening <code>index.html</code> directly is not enough.</p>" +
      '<pre class="code-block">python3 learning/study/serve.py</pre>' +
      '<p class="lede">Then open <code>http://127.0.0.1:8765/</code> and reload.</p>' +
      '<p class="meta">' + esc(error && error.message ? error.message : "unknown error") + "</p>" +
      details +
      "</div></section>";
  }

  function setupSolveIndex() {
    try {
      const saved = window.localStorage.getItem(PROBLEM_KEY) || "";
      const colon = saved.indexOf(":");
      let source = "curated";
      let id = saved;
      if (colon > 0) {
        const prefix = saved.slice(0, colon);
        if (prefix === "curated" || prefix === "practice") {
          source = prefix;
          id = saved.slice(colon + 1);
        }
      }
      const list = source === "practice" ? PRACTICE : PROBLEMS;
      const index = list.findIndex(function (item) { return item.id === id; });
      if (index >= 0) {
        state.solve.source = source;
        state.solve.index = index;
      }
    } catch (err) {}
  }

  function bootView() {
    state.loaded = true;
    const bootHash = (window.location.hash || "").replace("#", "");
    if (!ITEMS.length && !PROBLEMS.length && !PRACTICE.length) {
      els.view.innerHTML =
        '<section class="row hero empty"><div>' +
        '<p class="eyebrow">No content</p>' +
        "<h1>The content files are empty.</h1>" +
        '<p class="lede">Add drills to <code>learning/study_bank.py</code> or problems to ' +
        "<code>learning/solve_bank.py</code>.</p>" +
        "</div></section>";
      renderChrome();
      return;
    }
    if (bootHash === "session") {
      startSession();
    } else if (bootHash === "solve") {
      state.view = "solve";
      render();
    } else if (bootHash === "graph") {
      state.view = "graph";
      render();
    } else if (bootHash === "cheatsheet") {
      state.view = "cheatsheet";
      render();
    } else {
      render();
    }
  }

  state.canStore = detectStorage();
  state.progress = loadProgress();
  state.notes = loadNotes();
  initTheme();
  window.addEventListener("beforeunload", persistNotes);
  window.addEventListener("resize", function () {
    if (state.view === "graph") drawGraph();
  });

  showLoading();
  loadContent()
    .then(function (content) {
      ITEMS = content.items || [];
      CONCEPTS = content.concepts || [];
      PROBLEMS = content.problems || [];
      PRACTICE = content.practice || [];
      CHEATS = content.cheatsheet || [];
      GRAPH = content.graph || { nodes: [], edges: [] };
      setupSolveIndex();
      bootView();
    })
    .catch(showLoadError);
})();
