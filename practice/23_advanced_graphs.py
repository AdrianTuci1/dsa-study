"""
CONCEPT: Advanced Graphs I (Dijkstra, MST, Bellman-Ford with K stops)

Soluții de referință — toate testele trec. Citește-le, apoi încearcă să le
rescrii din memorie fără să te uiți. Verifică astfel:

    python3 practice/23_advanced_graphs.py

Output: [v] test trecut, [x] test picat, la final N/M passed.
"""
import heapq

from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Network Delay Time  (LeetCode 743, 0-indexed variant)
#
# Every problem in this file uses 0-indexed node numbers: nodes go from 0 to
# n-1 (the original LeetCode statement numbers nodes from 1 to n).
#
# Nodes are numbered 0 .. n-1. `times` is a list of directed edges [u, v, w]:
# a signal leaving u arrives at v after w units of time. The signal starts at
# `source` at time 0. Return the time at which the last node receives the
# signal, i.e. the largest shortest-path distance from `source`, or -1 if some
# node can never be reached. With a single node the answer is 0.
#
# Example 1:
#   Input: n = 4, times = [[1, 0, 1], [1, 2, 1], [2, 3, 1]], source = 1
#   Output: 2
#   Explanation: node 1 at time 0, nodes 0 and 2 at time 1, node 3 at time 2,
#   so every node has the signal after 2 units of time.
# Example 2:
#   Input: n = 2, times = [[0, 1, 1]], source = 0
#   Output: 1
# Example 3:
#   Input: n = 2, times = [[0, 1, 1]], source = 1
#   Output: -1
#   Explanation: the only edge leaves node 0, so node 1 never gets the signal.
#
# Constraints:
#   - 1 <= n <= 100
#   - 0 <= len(times) <= 6000
#   - Every edge is [u, v, w] with 0 <= u, v < n and 0 <= w <= 100
#   - 0 <= source < n
# ---------------------------------------------------------------------------
def p1_network_delay_time(n, times, source):
    # Dijkstra from source (all weights are >= 0). The answer is the largest
    # finalised distance; an unreachable node stays at infinity.
    graph = [[] for _ in range(n)]
    for u, v, w in times:
        graph[u].append((v, w))

    INF = float("inf")
    dist = [INF] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # stale heap entry
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    longest = max(dist)
    return -1 if longest == INF else longest


# ---------------------------------------------------------------------------
# Problem 2 - Min Cost to Connect All Points  (LeetCode 1584)
#
# `points` is a list of [x, y] integer coordinates. Connecting two points
# costs their Manhattan distance |x1 - x2| + |y1 - y2|, and every pair of
# points may be connected directly. Return the minimum total cost of a set of
# connections that makes all points connected (a minimum spanning tree).
# With 0 or 1 point the cost is 0; duplicate points are allowed and cost 0 to
# connect to each other.
#
# Example 1:
#   Input: points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
#   Output: 20
#   Explanation: connect [0,0]-[2,2] (4), [2,2]-[5,2] (3), [5,2]-[7,0] (4)
#   and [2,2]-[3,10] (9), for a total of 20.
# Example 2:
#   Input: points = [[3, 12], [-2, 5], [-4, 1]]
#   Output: 18
#   Explanation: costs are 12, 18 and 6, so the two cheapest edges already
#   form a spanning tree.
#
# Constraints:
#   - 0 <= len(points) <= 1000
#   - Every point is [x, y] with -10^6 <= x, y <= 10^6
# ---------------------------------------------------------------------------
def p2_min_cost_connect_points(points):
    # The graph is complete (every pair may be connected), so Prim's O(n^2)
    # "pick the cheapest crossing edge" is simpler than sorting ~n^2/2 edges.
    n = len(points)
    if n <= 1:
        return 0

    def distance(i, j):
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

    INF = float("inf")
    best = [INF] * n  # cheapest edge from the tree to each point
    used = [False] * n
    best[0] = 0
    total = 0
    for _ in range(n):
        u = -1
        for i in range(n):
            if not used[i] and (u == -1 or best[i] < best[u]):
                u = i
        used[u] = True
        total += best[u]
        for v in range(n):
            if not used[v]:
                d = distance(u, v)
                if d < best[v]:
                    best[v] = d
    return total


# ---------------------------------------------------------------------------
# Problem 3 - Cheapest Flights Within K Stops  (LeetCode 787)
#
# Cities are numbered 0 .. n-1. `flights` is a list of directed edges
# [from, to, price]. Return the cheapest price of a route from `src` to `dst`
# that makes at most `k` stops, where a stop is an intermediate city (so at
# most k + 1 flights). Return -1 if no such route exists, and 0 if
# src == dst. Every price is positive, so revisiting a city never helps.
#
# Example 1:
#   Input: n = 4,
#          flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600],
#                     [2, 3, 200]],
#          src = 0, dst = 3, k = 1
#   Output: 700
#   Explanation: 0 -> 1 -> 3 costs 700 and has 1 stop; the cheaper route
#   0 -> 1 -> 2 -> 3 costs 400 but has 2 stops, more than k = 1.
# Example 2:
#   Input: n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
#          src = 0, dst = 2, k = 1
#   Output: 200
#   Explanation: 0 -> 1 -> 2 costs 200, one stop.
# Example 3:
#   Input: n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
#          src = 0, dst = 2, k = 0
#   Output: 500
#   Explanation: with no stop allowed, only the direct flight is possible.
#
# Constraints:
#   - 1 <= n <= 100
#   - 0 <= len(flights) <= 6000
#   - Every flight is [from, to, price] with 0 <= from, to < n,
#     from != to and 1 <= price <= 10000
#   - 0 <= src, dst < n and 0 <= k < n
# ---------------------------------------------------------------------------
def p3_find_cheapest_price(n, flights, src, dst, k):
    # Bellman-Ford limited to k + 1 rounds (one round == one more flight).
    # Relaxing from a copy of the previous round's distances is what enforces
    # the "at most k stops" limit; relaxing in place would allow longer paths.
    if src == dst:
        return 0
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):
        nxt = dist[:]
        for u, v, price in flights:
            if dist[u] != INF and dist[u] + price < nxt[v]:
                nxt[v] = dist[u] + price
        dist = nxt
    return -1 if dist[dst] == INF else dist[dst]


if __name__ == "__main__":
    tests = [
        ("P1 network_delay_time", p1_network_delay_time,
         (4, [[1, 0, 1], [1, 2, 1], [2, 3, 1]], 1), 2),
        ("P1 network_delay_time", p1_network_delay_time, (2, [[0, 1, 1]], 0), 1),
        ("P1 network_delay_time", p1_network_delay_time, (2, [[0, 1, 1]], 1), -1),
        ("P1 network_delay_time", p1_network_delay_time, (1, [], 0), 0),
        ("P1 network_delay_time", p1_network_delay_time,
         (4, [[0, 1, 1], [2, 3, 1]], 0), -1),
        ("P1 network_delay_time", p1_network_delay_time,
         (2, [[0, 1, 5], [0, 1, 2]], 0), 2),
        ("P1 network_delay_time", p1_network_delay_time, (2, [[0, 0, 0]], 0), -1),
        ("P1 network_delay_time", p1_network_delay_time,
         (3, [[0, 1, 0], [1, 2, 0]], 0), 0),
        ("P1 network_delay_time", p1_network_delay_time,
         (5, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [0, 4, 10]], 0), 4),
        ("P2 min_cost_connect_points", p2_min_cost_connect_points,
         ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],), 20),
        ("P2 min_cost_connect_points", p2_min_cost_connect_points,
         ([[3, 12], [-2, 5], [-4, 1]],), 18),
        ("P2 min_cost_connect_points", p2_min_cost_connect_points, ([],), 0),
        ("P2 min_cost_connect_points", p2_min_cost_connect_points, ([[0, 0]],), 0),
        ("P2 min_cost_connect_points", p2_min_cost_connect_points,
         ([[0, 0], [0, 0]],), 0),
        ("P2 min_cost_connect_points", p2_min_cost_connect_points,
         ([[0, 0], [1, 1]],), 2),
        ("P2 min_cost_connect_points", p2_min_cost_connect_points,
         ([[0, 0], [1, 0], [2, 0]],), 2),
        ("P2 min_cost_connect_points", p2_min_cost_connect_points,
         ([[0, 0], [5, 5], [10, 0]],), 20),
        ("P2 min_cost_connect_points", p2_min_cost_connect_points,
         ([[0, 0], [1, 3], [2, 1], [4, 4], [5, 2]],), 13),
        ("P3 find_cheapest_price", p3_find_cheapest_price,
         (4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
          0, 3, 1), 700),
        ("P3 find_cheapest_price", p3_find_cheapest_price,
         (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1), 200),
        ("P3 find_cheapest_price", p3_find_cheapest_price,
         (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0), 500),
        ("P3 find_cheapest_price", p3_find_cheapest_price, (2, [], 0, 0, 0), 0),
        ("P3 find_cheapest_price", p3_find_cheapest_price, (2, [], 0, 1, 0), -1),
        ("P3 find_cheapest_price", p3_find_cheapest_price, (2, [[0, 1, 100]], 0, 1, 0), 100),
        ("P3 find_cheapest_price", p3_find_cheapest_price,
         (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1]], 0, 3, 1), -1),
        ("P3 find_cheapest_price", p3_find_cheapest_price,
         (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 100]], 0, 3, 1), 100),
        ("P3 find_cheapest_price", p3_find_cheapest_price,
         (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 100]], 0, 3, 2), 3),
        ("P3 find_cheapest_price", p3_find_cheapest_price,
         (3, [[0, 1, 1], [0, 1, 5], [1, 2, 1]], 0, 2, 1), 2),
        ("P3 find_cheapest_price", p3_find_cheapest_price,
         (3, [[0, 1, 5], [1, 2, 5]], 0, 2, 0), -1),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
