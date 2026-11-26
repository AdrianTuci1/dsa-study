"""
CONCEPT: String Algorithms (KMP, rolling hash, Manacher)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/26_string_algorithms.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Find the Index of the First Occurrence in a String
#             (LeetCode 28)
#
# Given two strings `haystack` and `needle`, return the index of the first
# occurrence of `needle` in `haystack`, or -1 if `needle` is not part of
# `haystack`. An empty `needle` occurs at index 0. Matches may overlap: in
# "aaaaa" the needle "aaaa" occurs both at index 0 and at index 1, and the
# first occurrence (0) is the answer.
#
# Implement KMP (Knuth-Morris-Pratt) with a prefix table ("failure function").
# The naive scan that restarts from scratch after every mismatch is NOT
# accepted: your solution must run in O(n + m) time, where n = len(haystack)
# and m = len(needle).
#
# Example 1:
#   Input: haystack = "sadbutsad", needle = "sad"
#   Output: 0
#   Explanation: "sad" occurs at index 0 and at index 6; the first one is 0.
# Example 2:
#   Input: haystack = "leetcode", needle = "leeto"
#   Output: -1
#   Explanation: "leeto" never occurs in "leetcode".
#
# Constraints:
#   - 0 <= len(haystack) <= 10^4
#   - 0 <= len(needle) <= 10^4
#   - haystack and needle consist of lowercase English letters.
# ---------------------------------------------------------------------------
def p1_str_str(haystack, needle):
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Problem 2 - Repeated DNA Sequences  (LeetCode 187)
#
# A DNA sequence is a string over the alphabet {'A', 'C', 'G', 'T'}. A
# 10-letter-long sequence is a substring of exactly 10 characters. Return every
# 10-letter-long sequence that occurs more than once in `s`, sorted in
# lexicographic order (that sorted order is part of the requirement - do not
# return them in an arbitrary order).
#
# The intended technique is a Rabin-Karp rolling hash: encode the bases as
# digits in base 4 and slide a hash over the string, updating it in O(1) per
# position (a set of all 10-length windows is a valid fallback, but the rolling
# hash is what this problem trains).
#
# Example 1:
#   Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#   Output: ["AAAAACCCCC", "CCCCCAAAAA"]
#   Explanation: "AAAAACCCCC" occurs at indices 0 and 10, "CCCCCAAAAA" at
#     indices 5 and 16; no other 10-letter-long sequence repeats.
# Example 2:
#   Input: s = "AAAAAAAAAAA"
#   Output: ["AAAAAAAAAA"]
#   Explanation: the string has length 11, so "AAAAAAAAAA" occurs twice (at
#     indices 0 and 1).
#
# Constraints:
#   - 0 <= len(s) <= 10^5
#   - s consists of the characters 'A', 'C', 'G', 'T'.
#   - A string shorter than 10 characters has no such sequence.
# ---------------------------------------------------------------------------
def p2_find_repeated_dna_sequences(s):
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Problem 3 - Longest Palindromic Substring  (LeetCode 5)
#
# Given a string `s`, return the longest palindromic substring of `s`. A
# substring is a contiguous part of `s`.
#
# Implement Manacher's algorithm, which finds the answer in O(n) time by
# reusing previously computed palindrome radii (typically on a transformed
# string such as "#a#b#a#", where every palindrome becomes odd-length). The
# O(n^2) expand-around-center version is NOT accepted.
#
# Example 1:
#   Input: s = "cbbd"
#   Output: "bb"
# Example 2:
#   Input: s = "forgeeksskeegfor"
#   Output: "geeksskeeg"
#
# Constraints:
#   - 0 <= len(s) <= 1000
#   - s consists of lowercase English letters.
#   - When several substrings share the maximum length, any of them is a valid
#     answer; every test below is chosen so that the longest palindromic
#     substring is unique.
# ---------------------------------------------------------------------------
def p3_longest_palindrome(s):
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    tests = [
        ("P1 str_str", p1_str_str, ("sadbutsad", "sad"), 0),
        ("P1 str_str absent", p1_str_str, ("leetcode", "leeto"), -1),
        ("P1 str_str empty needle", p1_str_str, ("abc", ""), 0),
        ("P1 str_str empty haystack", p1_str_str, ("", "abc"), -1),
        ("P1 str_str overlapping", p1_str_str, ("aaaaa", "aaaa"), 0),
        ("P1 str_str overlap fallback", p1_str_str, ("aaaaab", "aaaab"), 1),
        ("P1 str_str prefix fallback", p1_str_str, ("aabaabaaac", "aabaaac"), 3),
        ("P1 str_str single char", p1_str_str, ("a", "a"), 0),
        ("P1 str_str later match", p1_str_str, ("mississippi", "issip"), 4),
        ("P1 str_str identical", p1_str_str, ("abc", "abc"), 0),
        ("P2 repeated_dna", p2_find_repeated_dna_sequences,
         ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",), ["AAAAACCCCC", "CCCCCAAAAA"]),
        ("P2 repeated_dna periodic", p2_find_repeated_dna_sequences,
         ("ACGTACGTACGTACGTACGT",),
         ["ACGTACGTAC", "CGTACGTACG", "GTACGTACGT", "TACGTACGTA"]),
        ("P2 repeated_dna length 11", p2_find_repeated_dna_sequences,
         ("AAAAAAAAAAA",), ["AAAAAAAAAA"]),
        ("P2 repeated_dna too short", p2_find_repeated_dna_sequences,
         ("ACGTACGT",), []),
        ("P2 repeated_dna single window", p2_find_repeated_dna_sequences,
         ("ACGTACGTAC",), []),
        ("P2 repeated_dna empty", p2_find_repeated_dna_sequences, ("",), []),
        ("P2 repeated_dna blocks", p2_find_repeated_dna_sequences,
         ("GGGGGGGGGGACGTACGTACGGGGGGGGGG",), ["GGGGGGGGGG"]),
        ("P3 longest_palindrome even", p3_longest_palindrome, ("cbbd",), "bb"),
        ("P3 longest_palindrome", p3_longest_palindrome, ("forgeeksskeegfor",), "geeksskeeg"),
        ("P3 longest_palindrome single char", p3_longest_palindrome, ("a",), "a"),
        ("P3 longest_palindrome empty", p3_longest_palindrome, ("",), ""),
        ("P3 longest_palindrome all equal", p3_longest_palindrome, ("aaaa",), "aaaa"),
        ("P3 longest_palindrome at start", p3_longest_palindrome, ("abac",), "aba"),
        ("P3 longest_palindrome inner", p3_longest_palindrome, ("zabcddcbae",), "abcddcba"),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
