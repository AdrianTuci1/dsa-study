"""
CONCEPT: Design (data structures)

Soluții de referință — toate testele trec. Citește-le, apoi încearcă să le
rescrii din memorie fără să te uiți. Verifică astfel:

    python3 practice/20_design.py

Output: [v] test trecut, [x] test picat, la final N/M passed.
"""
from collections import OrderedDict

from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - LRU Cache  (LeetCode 146)
#
# Design a cache with a fixed positive `capacity` that evicts the Least
# Recently Used key when it runs out of space.
#
# Operations:
#   - "LRUCache" (constructor, args [capacity]): create an empty cache.
#   - get(key): return the value of the key, or -1 if absent. A successful get
#     makes the key the most recently used.
#   - put(key, value): insert or update the key and mark it most recently used.
#     Updating an existing key does not change the number of stored keys.
#     If the number of keys exceeds capacity, evict the least recently used one.
#
# Example 1:
#   Input: ops  = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#          args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#   Output: [None, None, None, 1, None, -1, None, -1, 3, 4]
#   Explanation: capacity 2; put(3, 3) evicts key 2, put(4, 4) evicts key 1.
# Example 2:
#   Input: ops  = ["LRUCache", "put", "get", "put", "get", "get"]
#          args = [[1], [1, 10], [1], [2, 20], [1], [2]]
#   Output: [None, None, 10, None, -1, 20]
#   Explanation: capacity 1, so put(2, 20) evicts the only stored key.
#
# Constraints:
#   - 1 <= capacity <= 100
#   - 1 <= len(ops) <= 1000
#   - 0 <= key, value <= 1000
#   - get and put are only called after the constructor
# ---------------------------------------------------------------------------
def p1_lru_cache(ops, args):
    """ops: list of operation names. args: list of argument lists, same length.
    Return a list with one result per operation: None for the constructor,
    otherwise the operation's return value (None when it returns nothing).

    Example:
      ops  = ["LRUCache", "put", "put", "get", "put", "get"]
      args = [[2], [1, 1], [2, 2], [1], [3, 3], [2]]
      -> [None, None, None, 1, None, -1]
    """
    cache = None
    capacity = 0
    out = []
    for op, a in zip(ops, args):
        if op == "LRUCache":
            capacity = a[0]
            cache = OrderedDict()  # least recently used key at the front
            out.append(None)
        elif op == "get":
            key = a[0]
            if key not in cache:
                out.append(-1)
            else:
                cache.move_to_end(key)  # a read makes it most recently used
                out.append(cache[key])
        elif op == "put":
            key, value = a
            if key in cache:
                cache.move_to_end(key)  # update also refreshes the key
            cache[key] = value
            if len(cache) > capacity:
                cache.popitem(last=False)  # evict the least recently used
            out.append(None)
    return out


# ---------------------------------------------------------------------------
# Problem 2 - Min Stack  (LeetCode 155)
#
# Design a stack that supports push, pop, top and retrieving the minimum
# element, each in O(1) time.
#
# Operations:
#   - "MinStack" (constructor, args []): create an empty stack.
#   - push(val): push val on top of the stack; returns nothing.
#   - pop(): remove the top element; returns nothing.
#   - top(): return the top element.
#   - getMin(): return the minimum element currently in the stack.
#
# Example 1:
#   Input: ops  = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
#          args = [[], [-2], [0], [-3], [], [], [], []]
#   Output: [None, None, None, None, -3, None, 0, -2]
# Example 2:
#   Input: ops  = ["MinStack", "push", "top", "getMin", "pop", "push", "getMin"]
#          args = [[], [5], [], [], [], [2], []]
#   Output: [None, None, 5, 5, None, None, 2]
#
# Constraints:
#   - 1 <= len(ops) <= 1000
#   - -1000 <= val <= 1000
#   - pop, top and getMin are only called when the stack is non-empty
# ---------------------------------------------------------------------------
def p2_min_stack(ops, args):
    """ops: list of operation names. args: list of argument lists, same length.
    Return a list with one result per operation: None for the constructor,
    otherwise the operation's return value (None when it returns nothing).
    """
    stack = []
    mins = []  # mins[i] = minimum of stack[0..i]
    out = []
    for op, a in zip(ops, args):
        if op == "MinStack":
            out.append(None)
        elif op == "push":
            value = a[0]
            stack.append(value)
            mins.append(value if not mins else min(value, mins[-1]))
            out.append(None)
        elif op == "pop":
            stack.pop()
            mins.pop()
            out.append(None)
        elif op == "top":
            out.append(stack[-1])
        elif op == "getMin":
            out.append(mins[-1])
    return out


# ---------------------------------------------------------------------------
# Problem 3 - Implement Queue using Stacks  (LeetCode 232)
#
# Design a first-in-first-out (FIFO) queue using only two stacks (push on top,
# pop and peek from the top of a stack).
#
# Operations:
#   - "MyQueue" (constructor, args []): create an empty queue.
#   - push(x): push x to the back of the queue; returns nothing.
#   - pop(): remove and return the element at the front of the queue.
#   - peek(): return the element at the front of the queue.
#   - empty(): True if the queue is empty, False otherwise.
#
# Example 1:
#   Input: ops  = ["MyQueue", "push", "push", "peek", "pop", "empty"]
#          args = [[], [1], [2], [], [], []]
#   Output: [None, None, None, 1, 1, False]
# Example 2:
#   Input: ops  = ["MyQueue", "push", "push", "push", "pop", "pop", "pop"]
#          args = [[], [1], [2], [3], [], [], []]
#   Output: [None, None, None, None, 1, 2, 3]
#
# Constraints:
#   - 1 <= len(ops) <= 1000
#   - -1000 <= x <= 1000
#   - pop and peek are only called when the queue is non-empty
# ---------------------------------------------------------------------------
def p3_queue_with_stacks(ops, args):
    """ops: list of operation names. args: list of argument lists, same length.
    Return a list with one result per operation: None for the constructor,
    otherwise the operation's return value (None when it returns nothing).
    """
    inbox = []   # newest elements on top
    outbox = []  # oldest elements on top; refilled by pouring inbox into it
    out = []
    for op, a in zip(ops, args):
        if op == "MyQueue":
            out.append(None)
        elif op == "push":
            inbox.append(a[0])
            out.append(None)
        elif op in ("pop", "peek"):
            # Pour only when the outbox is empty: every element moves once,
            # so push is O(1) and pop/peek are amortised O(1).
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            out.append(outbox.pop() if op == "pop" else outbox[-1])
        elif op == "empty":
            out.append(not inbox and not outbox)
    return out


if __name__ == "__main__":
    tests = [
        # ---- Problem 1: LRU Cache -----------------------------------------
        ("P1 lru example", p1_lru_cache,
         (["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
          [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]),
         [None, None, None, 1, None, -1, None, -1, 3, 4]),
        ("P1 lru capacity one", p1_lru_cache,
         (["LRUCache", "put", "get", "put", "get", "get"],
          [[1], [1, 10], [1], [2, 20], [1], [2]]),
         [None, None, 10, None, -1, 20]),
        ("P1 lru get missing", p1_lru_cache,
         (["LRUCache", "get", "put", "get"],
          [[1], [1], [1, 5], [1]]),
         [None, -1, None, 5]),
        ("P1 lru update keeps size", p1_lru_cache,
         (["LRUCache", "put", "put", "put", "get", "get"],
          [[2], [1, 1], [2, 2], [1, 9], [1], [2]]),
         [None, None, None, None, 9, 2]),
        ("P1 lru update refreshes order", p1_lru_cache,
         (["LRUCache", "put", "put", "put", "put", "get", "get"],
          [[2], [1, 1], [2, 2], [1, 5], [3, 3], [1], [2]]),
         [None, None, None, None, None, 5, -1]),
        ("P1 lru eviction order", p1_lru_cache,
         (["LRUCache", "put", "put", "put", "get", "put", "get", "get", "get"],
          [[3], [1, 1], [2, 2], [3, 3], [2], [4, 4], [1], [2], [4]]),
         [None, None, None, None, 2, None, -1, 2, 4]),
        # ---- Problem 2: Min Stack -----------------------------------------
        ("P2 min_stack example", p2_min_stack,
         (["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
          [[], [-2], [0], [-3], [], [], [], []]),
         [None, None, None, None, -3, None, 0, -2]),
        ("P2 min_stack single element", p2_min_stack,
         (["MinStack", "push", "top", "getMin", "pop", "push", "top", "getMin"],
          [[], [5], [], [], [], [2], [], []]),
         [None, None, 5, 5, None, None, 2, 2]),
        ("P2 min_stack duplicate min", p2_min_stack,
         (["MinStack", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
          [[], [1], [1], [1], [], [], [], [], []]),
         [None, None, None, None, 1, None, 1, None, 1]),
        ("P2 min_stack popping minimum", p2_min_stack,
         (["MinStack", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
          [[], [3], [2], [1], [], [], [], [], []]),
         [None, None, None, None, 1, None, 2, None, 3]),
        ("P2 min_stack reuse after empty", p2_min_stack,
         (["MinStack", "push", "push", "pop", "pop", "push", "getMin", "top"],
          [[], [4], [0], [], [], [7], [], []]),
         [None, None, None, None, None, None, 7, 7]),
        # ---- Problem 3: Queue using Stacks --------------------------------
        ("P3 queue example", p3_queue_with_stacks,
         (["MyQueue", "push", "push", "peek", "pop", "empty"],
          [[], [1], [2], [], [], []]),
         [None, None, None, 1, 1, False]),
        ("P3 queue empty at start", p3_queue_with_stacks,
         (["MyQueue", "empty", "push", "empty"],
          [[], [], [5], []]),
         [None, True, None, False]),
        ("P3 queue interleaved", p3_queue_with_stacks,
         (["MyQueue", "push", "pop", "empty", "push", "peek", "push", "pop", "pop", "empty"],
          [[], [1], [], [], [2], [], [3], [], [], []]),
         [None, None, 1, True, None, 2, None, 2, 3, True]),
        ("P3 queue fifo order", p3_queue_with_stacks,
         (["MyQueue", "push", "push", "push", "pop", "pop", "pop"],
          [[], [1], [2], [3], [], [], []]),
         [None, None, None, None, 1, 2, 3]),
        ("P3 queue push between pops", p3_queue_with_stacks,
         (["MyQueue", "push", "push", "pop", "push", "pop", "push", "pop", "pop", "empty"],
          [[], [1], [2], [], [3], [], [4], [], [], []]),
         [None, None, None, 1, None, 2, None, 3, 4, True]),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
