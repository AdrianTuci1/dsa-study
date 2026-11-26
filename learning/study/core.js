/* Pure logic for the study app: scheduling, selection, matching, stats.
 *
 * No DOM access here, so the same file runs in the browser and in Node
 * (`node learning/study/test_core.js`).
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api;
  } else {
    root.StudyCore = api;
  }
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  const DAY_MS = 86400000;

  // --- dates (local calendar days, stored as YYYY-MM-DD) -----------------
  function pad(n) {
    return String(n).padStart(2, "0");
  }

  function todayISO(date) {
    const d = date || new Date();
    return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate());
  }

  function parseISO(iso) {
    const parts = String(iso).split("-");
    return new Date(Number(parts[0]), Number(parts[1]) - 1, Number(parts[2]));
  }

  function addDaysISO(iso, days) {
    const d = parseISO(iso);
    d.setDate(d.getDate() + days);
    return todayISO(d);
  }

  function daysBetween(fromISO, toISO) {
    return Math.round((parseISO(toISO) - parseISO(fromISO)) / DAY_MS);
  }

  function round(value, places) {
    const factor = Math.pow(10, places);
    return Math.round(value * factor) / factor;
  }

  // --- answer checking ---------------------------------------------------
  // Whitespace-insensitive and case-insensitive; quotes are ignored so that
  // `'p'`, `"p"` and `p` all match. This is a recall tool, not a compiler.
  function normalize(text) {
    return String(text == null ? "" : text)
      .toLowerCase()
      .replace(/[\s"'`]+/g, "");
  }

  function matchesAnswer(given, answers) {
    const g = normalize(given);
    if (!g) return false;
    return (answers || []).some(function (answer) {
      return normalize(answer) === g;
    });
  }

  // --- SM-2 style scheduling --------------------------------------------
  // grade: 0 again, 1 hard, 2 good, 3 easy
  function schedule(grade, previous, today) {
    const prev = previous || {};
    const t = today || todayISO();
    let ease = prev.ease == null ? 2.5 : prev.ease;
    let reps = prev.reps || 0;
    let interval = prev.interval || 0;
    let lapses = prev.lapses || 0;

    if (grade === 0) {
      ease = Math.max(1.3, ease - 0.2);
      reps = 0;
      interval = 0;
      lapses += 1;
    } else {
      reps += 1;
      if (grade === 1) {
        ease = Math.max(1.3, ease - 0.15);
        interval = interval < 1 ? 1 : Math.max(1, interval * 1.2);
      } else if (grade === 2) {
        interval = reps === 1 ? 1 : Math.max(2, interval * ease);
      } else {
        ease = Math.min(2.8, ease + 0.15);
        interval = reps === 1 ? 1 : Math.max(2, interval * ease * 1.3);
      }
    }

    return {
      ease: round(ease, 2),
      reps: reps,
      interval: round(interval, 1),
      lapses: lapses,
      due: addDaysISO(t, Math.round(interval)),
      lastGrade: grade,
    };
  }

  // --- progress ----------------------------------------------------------
  function emptyProgress() {
    return {
      version: 1,
      items: {},
      history: {},
      solved: {},
      settings: { goal: 20, limit: 20, concept: "" },
    };
  }

  function ensureProgress(progress) {
    const p = progress && typeof progress === "object" ? progress : emptyProgress();
    if (!p.items || typeof p.items !== "object") p.items = {};
    if (!p.history || typeof p.history !== "object") p.history = {};
    if (!p.solved || typeof p.solved !== "object") p.solved = {};
    if (!p.settings || typeof p.settings !== "object") p.settings = {};
    if (!p.settings.goal) p.settings.goal = 20;
    if (!p.settings.limit) p.settings.limit = 20;
    if (typeof p.settings.concept !== "string") p.settings.concept = "";
    if (!p.version) p.version = 1;
    return p;
  }

  function recordResult(progress, item, grade, today) {
    const p = ensureProgress(progress);
    const t = today || todayISO();
    const prev = p.items[item.id] || {};
    const next = schedule(grade, prev, t);

    p.items[item.id] = {
      ease: next.ease,
      reps: next.reps,
      interval: next.interval,
      lapses: next.lapses,
      due: next.due,
      lastGrade: grade,
      lastSeen: t,
      correct: (prev.correct || 0) + (grade >= 2 ? 1 : 0),
      wrong: (prev.wrong || 0) + (grade === 0 ? 1 : 0),
    };

    const day = p.history[t] || { reviewed: 0, correct: 0 };
    day.reviewed += 1;
    if (grade >= 2) day.correct += 1;
    p.history[t] = day;
    return p;
  }

  // --- selection ---------------------------------------------------------
  function shuffle(list) {
    const out = list.slice();
    for (let i = out.length - 1; i > 0; i -= 1) {
      const j = Math.floor(Math.random() * (i + 1));
      const tmp = out[i];
      out[i] = out[j];
      out[j] = tmp;
    }
    return out;
  }

  // Round-robin over concepts so a 20-item session is not 20 DP cards.
  function interleaveByConcept(items) {
    const groups = new Map();
    items.forEach(function (item) {
      if (!groups.has(item.concept)) groups.set(item.concept, []);
      groups.get(item.concept).push(item);
    });
    const queues = Array.from(groups.values());
    const out = [];
    let added = true;
    while (added) {
      added = false;
      for (let i = 0; i < queues.length; i += 1) {
        if (queues[i].length) {
          out.push(queues[i].shift());
          added = true;
        }
      }
    }
    return out;
  }

  function isDue(progress, item, today) {
    const st = progress.items && progress.items[item.id];
    return Boolean(st) && st.due <= (today || todayISO());
  }

  function buildSession(items, progress, options) {
    const opts = options || {};
    const p = ensureProgress(progress);
    const today = opts.today || todayISO();
    const concept = opts.concept || "";
    const limit = Math.max(1, opts.limit || 20);

    const pool = concept
      ? items.filter(function (item) { return item.concept === concept; })
      : items.slice();

    const due = [];
    const fresh = [];
    pool.forEach(function (item) {
      const st = p.items[item.id];
      if (!st) fresh.push(item);
      else if (st.due <= today) due.push(item);
    });

    due.sort(function (a, b) {
      const sa = p.items[a.id];
      const sb = p.items[b.id];
      if (sa.due !== sb.due) return sa.due < sb.due ? -1 : 1;
      return (sb.lapses || 0) - (sa.lapses || 0);
    });

    const ordered = interleaveByConcept(due).concat(interleaveByConcept(shuffle(fresh)));
    return ordered.slice(0, limit);
  }

  // --- stats -------------------------------------------------------------
  function streak(history, today) {
    const t = today || todayISO();
    let cursor = t;
    const todayEntry = history[cursor];
    if (!todayEntry || !todayEntry.reviewed) {
      cursor = addDaysISO(cursor, -1);
    }
    let count = 0;
    while (history[cursor] && history[cursor].reviewed > 0) {
      count += 1;
      cursor = addDaysISO(cursor, -1);
    }
    return count;
  }

  function computeStats(items, progress, today) {
    const p = ensureProgress(progress);
    const t = today || todayISO();
    const stats = {
      total: items.length,
      due: 0,
      fresh: 0,
      seen: 0,
      learning: 0,
      young: 0,
      mature: 0,
      todayReviewed: 0,
      todayCorrect: 0,
      streak: streak(p.history, t),
      goal: p.settings.goal || 20,
    };

    items.forEach(function (item) {
      const st = p.items[item.id];
      if (!st) {
        stats.fresh += 1;
        return;
      }
      stats.seen += 1;
      if (st.due <= t) stats.due += 1;
      if ((st.reps || 0) <= 1) stats.learning += 1;
      else if ((st.interval || 0) < 21) stats.young += 1;
      else stats.mature += 1;
    });

    const day = p.history[t];
    if (day) {
      stats.todayReviewed = day.reviewed || 0;
      stats.todayCorrect = day.correct || 0;
    }
    return stats;
  }

  function conceptRows(items, progress, today) {
    const p = ensureProgress(progress);
    const t = today || todayISO();
    const rows = new Map();

    items.forEach(function (item) {
      if (!rows.has(item.concept)) {
        rows.set(item.concept, {
          concept: item.concept,
          total: 0,
          due: 0,
          fresh: 0,
          mastered: 0,
          reviews: 0,
        });
      }
      const row = rows.get(item.concept);
      row.total += 1;
      const st = p.items[item.id];
      if (!st) {
        row.fresh += 1;
        row.due += 1; // new items are still work for today
        return;
      }
      if (st.due <= t) row.due += 1;
      if ((st.interval || 0) >= 21) row.mastered += 1;
      row.reviews += st.reps || 0;
    });

    return Array.from(rows.values());
  }

  function nextDueDate(items, progress) {
    const p = ensureProgress(progress);
    let best = null;
    items.forEach(function (item) {
      const st = p.items[item.id];
      if (!st) return;
      if (best === null || st.due < best) best = st.due;
    });
    return best;
  }

  return {
    DAY_MS: DAY_MS,
    todayISO: todayISO,
    addDaysISO: addDaysISO,
    daysBetween: daysBetween,
    normalize: normalize,
    matchesAnswer: matchesAnswer,
    schedule: schedule,
    emptyProgress: emptyProgress,
    ensureProgress: ensureProgress,
    recordResult: recordResult,
    buildSession: buildSession,
    isDue: isDue,
    interleaveByConcept: interleaveByConcept,
    shuffle: shuffle,
    streak: streak,
    computeStats: computeStats,
    conceptRows: conceptRows,
    nextDueDate: nextDueDate,
  };
});
