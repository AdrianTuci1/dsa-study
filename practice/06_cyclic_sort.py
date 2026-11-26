"""
CONCEPT: Cyclic Sort

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/06_cyclic_sort.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Missing Number  (LeetCode 268)
#
# Given a list of n distinct numbers taken from the range 0 to n, return the
# one number in that range that is missing from the list. The list is not
# sorted; you may reorder it in place or copy it.
#
# Example 1:
#   Input: nums = [3,0,1]
#   Output: 2
# Example 2:
#   Input: nums = [9,6,4,2,3,5,7,0,1]
#   Output: 8
#
# Constraints:
#   - 1 <= len(nums) <= 10^4
#   - every number in nums is unique
#   - nums contains n distinct values from 0 to n
# ---------------------------------------------------------------------------
def p1_missing(nums):
    n = len(nums)

    #asez fiecare valoare in casuta ei (valoarea v -> indexul v)
    i = 0
    while i < n:
        v = nums[i]
        if v < n and v != i:
            nums[v], nums[i] = nums[i], nums[v]
        else:
            i += 1

    #cine nu e la locul lui, acela e nr lipsa
    
    for i in range(n):
        if nums[i] != i:
            return i
    return n


def by_xor(nums):
    x = len(nums)
    for i, v in enumerate(nums):
        x ^= i ^ v
    return x


# ---------------------------------------------------------------------------
# Problem 2 - Find All Numbers Disappeared in an Array  (LeetCode 448)
#
# Given a list of n integers where each value is in the range 1 to n, return
# the list of values from 1 to n that do not appear. Some values may appear
# twice or more. The result must be sorted in increasing order.
#
# Example 1:
#   Input: nums = [4,3,2,7,8,2,3,1]
#   Output: [5,6]
# Example 2:
#   Input: nums = [1,1]
#   Output: [2]
#
# Constraints:
#   - 1 <= len(nums) <= 10^5
#   - 1 <= nums[i] <= len(nums)
# ---------------------------------------------------------------------------
def p2_disappeared(nums):
    n = len(nums)
    #aduc fiecare valoare in casa ei
    i = 0
    while i < n:
        home = nums[i] - 1
        if nums[i] != nums[home]: #casa lui are alta valoare -> am ce muta
            nums[home], nums[i] = nums[i], nums[home] 
        else:                          # casa lui are deja valoarea asta -> duplicat
            i += 1
    
    # casutele ocupate de un intrus = valorile lipsa
    return [v for v in range(1, n + 1) if nums[v - 1] !=v]


#marcare prin negare, fara swap-uri, doar semne
def p2_by_marking(nums):
    n = len(nums)
    for v in nums:
        idx = abs(v) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    return [i + 1 for i in range(n) if nums[i] > 0]
 

# ---------------------------------------------------------------------------
# Problem 3 - Find the Duplicate Number  (LeetCode 287)
#
# Given a list of n + 1 integers where each value is in the range 1 to n,
# return the one value that appears more than once. Exactly one value is
# repeated; you must not modify the original list.
#
# Example 1:
#   Input: nums = [1,3,4,2,2]
#   Output: 2
# Example 2:
#   Input: nums = [3,1,3,4,2]
#   Output: 3
#
# Constraints:
#   - 2 <= len(nums) <= 10^5
#   - 1 <= nums[i] <= len(nums) - 1
#   - exactly one value is repeated (possibly many times)
# ---------------------------------------------------------------------------
# two pointers floyd
def p3_duplicate(nums):
    # faza1: slow = 1 pas, fast = 2pasi > se intalnesc undeva in ciclu
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    #faza2: slow reporneste de la inceput, amandoi merg 1 pas > se intalnesc
    #la intrarea in ciclu
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow


#alta varianta 0(n)
def by_set(nums):
    seen = set()
    for v in nums:
        if v in seen:
            return v
        seen.add(v)




if __name__ == "__main__":
    tests = [
        ("P1 missing", p1_missing, ([3, 0, 1],), 2),
        ("P1 missing length 2", p1_missing, ([0, 1],), 2),
        ("P1 missing long", p1_missing, ([9, 6, 4, 2, 3, 5, 7, 0, 1],), 8),
        ("P1 missing single", p1_missing, ([0],), 1),
        ("P2 disappeared", p2_disappeared, ([4, 3, 2, 7, 8, 2, 3, 1],), [5, 6]),
        ("P2 disappeared pair", p2_disappeared, ([1, 1],), [2]),
        ("P2 disappeared none", p2_disappeared, ([1, 2, 3],), []),
        ("P2 disappeared all ones", p2_disappeared, ([1, 1, 1],), [2, 3]),
        ("P3 duplicate", p3_duplicate, ([1, 3, 4, 2, 2],), 2),
        ("P3 duplicate first", p3_duplicate, ([3, 1, 3, 4, 2],), 3),
        ("P3 duplicate pair", p3_duplicate, ([1, 1],), 1),
        ("P3 duplicate many", p3_duplicate, ([2, 2, 2, 2, 2],), 2),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
