/* Tests for core.js — run with: node learning/study/test_core.js */
"use strict";

const assert = require("assert");
const core = require("./core.js");

let checks = 0;

function test(name, fn) {
  fn();
  checks += 1;
  console.log("ok  " + name);
}

// ---------------------------------------------------------------- answers
test("normalize ignores case, whitespace and quotes", () => {
  assert.strictEqual(core.normalize("  Hi = MID "), "hi=mid");
  assert.strictEqual(core.normalize("'p'"), "p");
});

test("matchesAnswer accepts equivalent spellings", () => {
  assert.ok(core.matchesAnswer("hi = mid", ["hi = mid"]));
  assert.ok(core.matchesAnswer("hi=mid", ["hi = mid"]));
  assert.ok(core.matchesAnswer("[1,2,3]", ["[1, 2, 3]"]));
  assert.ok(core.matchesAnswer("p", ["'p'"]));
  assert.ok(!core.matchesAnswer("", ["x"]));
  assert.ok(!core.matchesAnswer("lo = mid", ["hi = mid"]));
});

// ---------------------------------------------------------------- dates
test("dates do not drift across month boundaries", () => {
  assert.strictEqual(core.addDaysISO("2026-01-31", 1), "2026-02-01");
  assert.strictEqual(core.addDaysISO("2026-03-01", -1), "2026-02-28");
  assert.strictEqual(core.daysBetween("2026-01-01", "2026-01-11"), 10);
});

// ---------------------------------------------------------------- schedule
test("schedule: good grows 1 -> 2.5 -> 6.3 days", () => {
  const today = "2026-11-26";
  let st = core.schedule(2, {}, today);
  assert.strictEqual(st.interval, 1);
  assert.strictEqual(st.reps, 1);
  assert.strictEqual(st.due, "2026-11-27");
  st = core.schedule(2, st, today);
  assert.strictEqual(st.interval, 2.5);
  st = core.schedule(2, st, today);
  assert.strictEqual(st.interval, 6.3);
});

test("schedule: again resets the interval and counts a lapse", () => {
  const today = "2026-11-26";
  let st = core.schedule(3, {}, today);
  st = core.schedule(3, st, today);
  const easeBefore = st.ease;
  st = core.schedule(0, st, today);
  assert.strictEqual(st.interval, 0);
  assert.strictEqual(st.reps, 0);
  assert.strictEqual(st.lapses, 1);
  assert.ok(st.ease < easeBefore);
});

test("schedule: easy is faster than good", () => {
  const today = "2026-11-26";
  let good = core.schedule(2, {}, today);
  good = core.schedule(2, good, today);
  let easy = core.schedule(3, {}, today);
  easy = core.schedule(3, easy, today);
  assert.ok(easy.interval > good.interval);
});

// ---------------------------------------------------------------- progress
test("recordResult updates item and history", () => {
  const today = "2026-11-26";
  const progress = core.emptyProgress();
  const item = { id: "x1" };
  core.recordResult(progress, item, 2, today);
  assert.strictEqual(progress.items.x1.reps, 1);
  assert.strictEqual(progress.history[today].reviewed, 1);
  assert.strictEqual(progress.history[today].correct, 1);

  core.recordResult(progress, item, 0, today);
  assert.strictEqual(progress.history[today].reviewed, 2);
  assert.strictEqual(progress.history[today].correct, 1);
  assert.strictEqual(progress.items.x1.lapses, 1);
});

// ---------------------------------------------------------------- selection
function makeItems() {
  return [
    { id: "a1", concept: "A" },
    { id: "a2", concept: "A" },
    { id: "b1", concept: "B" },
    { id: "c1", concept: "C" },
    { id: "c2", concept: "C" },
  ];
}

test("buildSession puts due items before new items", () => {
  const today = "2026-11-26";
  const progress = core.emptyProgress();
  // a1 is due yesterday, b1 due today, a2 due tomorrow, c1 seen future
  progress.items.a1 = { due: "2026-11-25", lapses: 0 };
  progress.items.b1 = { due: today, lapses: 0 };
  progress.items.a2 = { due: "2026-11-27", lapses: 0 };
  progress.items.c1 = { due: "2026-12-01", lapses: 0 };
  const session = core.buildSession(makeItems(), progress, { today: today, limit: 10 });
  const ids = session.map((item) => item.id);
  assert.deepStrictEqual(ids, ["a1", "b1", "c2"]);
});

test("buildSession respects concept, limit and round-robin", () => {
  const today = "2026-11-26";
  const progress = core.emptyProgress();
  const session = core.buildSession(makeItems(), progress, { today: today, concept: "A", limit: 10 });
  assert.deepStrictEqual(session.map((item) => item.id).sort(), ["a1", "a2"]);

  const limited = core.buildSession(makeItems(), progress, { today: today, limit: 3 });
  assert.strictEqual(limited.length, 3);

  const rr = core.interleaveByConcept([
    { id: "a1", concept: "A" },
    { id: "a2", concept: "A" },
    { id: "a3", concept: "A" },
    { id: "b1", concept: "B" },
  ]);
  assert.deepStrictEqual(rr.map((item) => item.id), ["a1", "b1", "a2", "a3"]);
});

test("buildSession returns empty when nothing is due", () => {
  const today = "2026-11-26";
  const progress = core.emptyProgress();
  makeItems().forEach((item) => {
    progress.items[item.id] = { due: "2026-12-10", lapses: 0 };
  });
  assert.deepStrictEqual(core.buildSession(makeItems(), progress, { today: today }), []);
});

// ---------------------------------------------------------------- stats
test("streak counts consecutive days, tolerating today not being done yet", () => {
  const history = {
    "2026-11-23": { reviewed: 2 },
    "2026-11-24": { reviewed: 1 },
    "2026-11-25": { reviewed: 4 },
  };
  assert.strictEqual(core.streak(history, "2026-11-26"), 3);
  history["2026-11-26"] = { reviewed: 1 };
  assert.strictEqual(core.streak(history, "2026-11-26"), 4);
  delete history["2026-11-25"];
  assert.strictEqual(core.streak(history, "2026-11-26"), 1);
});

test("computeStats separates fresh, due, learning and mature", () => {
  const today = "2026-11-26";
  const progress = core.emptyProgress();
  progress.items.a1 = { due: "2026-11-25", reps: 3, interval: 30 };
  progress.items.b1 = { due: "2026-11-27", reps: 1, interval: 1 };
  progress.items.c1 = { due: "2026-12-30", reps: 4, interval: 40 };
  progress.settings.goal = 20;
  const stats = core.computeStats(makeItems(), progress, today);
  assert.strictEqual(stats.due, 1);
  assert.strictEqual(stats.fresh, 2);
  assert.strictEqual(stats.seen, 3);
  assert.strictEqual(stats.learning, 1);
  assert.strictEqual(stats.mature, 2);
  assert.strictEqual(stats.total, 5);
});

test("conceptRows counts new items as due work", () => {
  const today = "2026-11-26";
  const progress = core.emptyProgress();
  progress.items.a1 = { due: "2026-11-25", reps: 2, interval: 10 };
  const rows = core.conceptRows(makeItems(), progress, today);
  const rowA = rows.find((row) => row.concept === "A");
  assert.strictEqual(rowA.total, 2);
  assert.strictEqual(rowA.due, 2); // a1 due + a2 new
  assert.strictEqual(rowA.fresh, 1);
  assert.strictEqual(rowA.mastered, 0);
});

test("nextDueDate returns the earliest scheduled date", () => {
  const progress = core.emptyProgress();
  progress.items.a1 = { due: "2026-12-02" };
  progress.items.b1 = { due: "2026-11-28" };
  progress.items.c1 = { due: "2027-01-01" };
  assert.strictEqual(core.nextDueDate(makeItems(), progress), "2026-11-28");
});

console.log("\n" + checks + " tests passed");
