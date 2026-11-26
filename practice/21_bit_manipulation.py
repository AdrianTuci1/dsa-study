"""
CONCEPT: Bit Manipulation

Soluții de referință — toate testele trec. Citește-le, apoi încearcă să le
rescrii din memorie fără să te uiți. Verifică astfel:

    python3 practice/21_bit_manipulation.py

Output: [v] test trecut, [x] test picat, la final N/M passed.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Single Number  (LeetCode 136)
#
# Given a non-empty list `nums` in which every element appears exactly twice
# except for one element that appears exactly once, return that single
# element. Your solution must run in linear time and use O(1) extra space.
#
# Example 1:
#   Input: nums = [2, 2, 1]
#   Output: 1
# Example 2:
#   Input: nums = [4, 1, 2, 1, 2]
#   Output: 4
#   Explanation: 1 and 2 appear twice, so only 4 is left.
#
# Constraints:
#   - 1 <= len(nums) <= 3 * 10^4
#   - -3 * 10^4 <= nums[i] <= 3 * 10^4
#   - every element appears twice except for exactly one element
# ---------------------------------------------------------------------------
def p1_single_number(nums):
    # XOR is commutative/associative, x ^ x == 0 and x ^ 0 == x, so every
    # duplicated value cancels itself out and only the single value remains.
    result = 0
    for x in nums:
        result ^= x
    return result


# ---------------------------------------------------------------------------
# Problem 2 - Number of 1 Bits  (LeetCode 191)
#
# Given a non-negative integer `n`, treat it as an unsigned 32-bit value and
# return the number of bits set to 1 in its binary representation (also called
# the Hamming weight).
#
# Example 1:
#   Input: n = 11
#   Output: 3
#   Explanation: 11 in binary is 1011, which has three '1' bits.
# Example 2:
#   Input: n = 128
#   Output: 1
#   Explanation: 128 in binary is 10000000, which has one '1' bit.
#
# Constraints:
#   - 0 <= n <= 2^32 - 1
# ---------------------------------------------------------------------------
def p2_hamming_weight(n):
    # n & (n - 1) clears the lowest set bit, so the loop runs once per 1 bit
    # instead of once per bit position.
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


# ---------------------------------------------------------------------------
# Problem 3 - Reverse Bits  (LeetCode 190)
#
# Given a non-negative integer `n`, treat it as an unsigned 32-bit value and
# return the integer obtained by reversing the order of its 32 bits. The input
# and the return value are integers (not strings, not lists of bits).
#
# Example 1:
#   Input: n = 43261596
#   Output: 964176192
#   Explanation: 00000010100101000001111010011100 reversed is
#                00111001011110000010100101000000.
# Example 2:
#   Input: n = 4294967293
#   Output: 3221225471
#   Explanation: 11111111111111111111111111111101 reversed is
#                10111111111111111111111111111111.
#
# Constraints:
#   - 0 <= n <= 2^32 - 1
# ---------------------------------------------------------------------------
def p3_reverse_bits(n):
    # Take n's bits from the right and push them into the answer from the
    # left, 32 times, so bit i of n ends up at bit 31 - i.
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


if __name__ == "__main__":
    tests = [
        ("P1 single_number", p1_single_number, ([2, 2, 1],), 1),
        ("P1 single_number", p1_single_number, ([4, 1, 2, 1, 2],), 4),
        ("P1 single_number single element", p1_single_number, ([1],), 1),
        ("P1 single_number with zero", p1_single_number, ([0, 1, 1],), 0),
        ("P1 single_number with negatives", p1_single_number, ([-1, -1, -2],), -2),
        ("P1 single_number many pairs", p1_single_number, ([1, 1, 2, 2, 3],), 3),
        ("P2 hamming_weight", p2_hamming_weight, (11,), 3),
        ("P2 hamming_weight", p2_hamming_weight, (128,), 1),
        ("P2 hamming_weight zero", p2_hamming_weight, (0,), 0),
        ("P2 hamming_weight one", p2_hamming_weight, (1,), 1),
        ("P2 hamming_weight 2^31 - 1", p2_hamming_weight, (2147483647,), 31),
        ("P2 hamming_weight 2^32 - 1", p2_hamming_weight, (4294967295,), 32),
        ("P3 reverse_bits", p3_reverse_bits, (43261596,), 964176192),
        ("P3 reverse_bits", p3_reverse_bits, (4294967293,), 3221225471),
        ("P3 reverse_bits zero", p3_reverse_bits, (0,), 0),
        ("P3 reverse_bits one", p3_reverse_bits, (1,), 2147483648),
        ("P3 reverse_bits 2^31", p3_reverse_bits, (2147483648,), 1),
        ("P3 reverse_bits all ones", p3_reverse_bits, (4294967295,), 4294967295),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
