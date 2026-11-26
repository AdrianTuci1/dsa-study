"""
CONCEPT: Topological Sort (dependencies / course order)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/15_topological_sort.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Course Schedule  (LeetCode 207)
#
# There are `num_courses` courses numbered 0 .. num_courses-1. The list
# `prerequisites` contains pairs [a, b] meaning course b must be taken before
# course a. Return True if it is possible to finish all courses, i.e. if the
# dependency graph has no cycle.
#
# Example 1:
#   Input: num_courses = 2, prerequisites = [[1, 0]]
#   Output: True
# Example 2:
#   Input: num_courses = 2, prerequisites = [[1, 0], [0, 1]]
#   Output: False
#
# Constraints:
#   - 1 <= num_courses <= 2000
#   - 0 <= len(prerequisites) <= 5000
#   - Every pair is [a, b] with 0 <= a, b < num_courses and a != b
# ---------------------------------------------------------------------------
def p1_can_finish(num_courses, prerequisites):
    adj = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1
    
    queue = dequeue(i for i in range(num_courses) if indeg[i] == 0)
    done = 0
    while queue:
        u = queue.popleft()
        done += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    
    return done == num_courses


# ---------------------------------------------------------------------------
# Problem 2 - Course Schedule II  (LeetCode 210)
#
# Same setup as Problem 1. Return the lexicographically smallest valid order
# in which all courses can be taken, so the answer is deterministic. Return
# [] if no valid order exists.
#
# Example 1:
#   Input: num_courses = 2, prerequisites = [[1, 0]]
#   Output: [0, 1]
# Example 2:
#   Input: num_courses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
#   Output: [0, 1, 2, 3]
#
# Constraints:
#   - 1 <= num_courses <= 2000
#   - 0 <= len(prerequisites) <= 5000
#   - Every pair is [a, b] with 0 <= a, b < num_courses and a != b
# ---------------------------------------------------------------------------
def p2_find_order(num_courses, prerequisites):
    adj = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1

    frontier = [i for i in range(num_courses) if indeg[i] == 0]
    done = 0
    semesters = 0
    while frontier:
        semesters += 1
        nxt = []
        for u in frontier:
            done += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    nxt.append(v)
        frontier = nxt

    return semesters if done == num_courses else -1



# ---------------------------------------------------------------------------
# Problem 3 - Minimum Number of Semesters
#
# Same setup as Problem 1, but courses are taken in semesters: in one
# semester you may take any set of courses whose prerequisites are already
# finished. Return the minimum number of semesters needed to finish every
# course, or -1 if the dependencies contain a cycle.
#
# Example 1:
#   Input: num_courses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
#   Output: 3
# Example 2:
#   Input: num_courses = 3, prerequisites = [[1, 0], [2, 1]]
#   Output: 3
#
# Constraints:
#   - 1 <= num_courses <= 2000
#   - 0 <= len(prerequisites) <= 5000
#   - Every pair is [a, b] with 0 <= a, b < num_courses and a != b
# ---------------------------------------------------------------------------
def p3_min_semesters(num_courses, prerequisites):
    adj = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1

    frontier = [i for i in range(num_courses) if indeg[i] == 0]
    done = 0
    semesters = 0
    while frontier:
        semesters += 1
        nxt = []
        for u in frontier:
            done += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    nxt.append(v)
        frontier = nxt
    
    return semesters if done == num_courses else -1


 

if __name__ == "__main__":
    tests = [
        ("P1 can_finish", p1_can_finish, (2, [[1, 0]]), True),
        ("P1 can_finish", p1_can_finish, (2, [[1, 0], [0, 1]]), False),
        ("P1 can_finish", p1_can_finish, (1, []), True),
        ("P1 can_finish", p1_can_finish, (5, [[1, 4], [2, 4], [3, 1], [3, 2]]), True),
        ("P1 can_finish", p1_can_finish, (3, [[0, 1], [1, 2], [2, 0]]), False),
        ("P2 find_order", p2_find_order, (2, [[1, 0]]), [0, 1]),
        ("P2 find_order", p2_find_order, (4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [0, 1, 2, 3]),
        ("P2 find_order", p2_find_order, (2, [[1, 0], [0, 1]]), []),
        ("P2 find_order", p2_find_order, (1, []), [0]),
        ("P2 find_order", p2_find_order, (3, []), [0, 1, 2]),
        ("P3 min_semesters", p3_min_semesters, (4, [[1, 0], [2, 0], [3, 1], [3, 2]]), 3),
        ("P3 min_semesters", p3_min_semesters, (3, [[1, 0], [2, 1]]), 3),
        ("P3 min_semesters", p3_min_semesters, (1, []), 1),
        ("P3 min_semesters", p3_min_semesters, (4, []), 1),
        ("P3 min_semesters", p3_min_semesters, (2, [[1, 0], [0, 1]]), -1),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
