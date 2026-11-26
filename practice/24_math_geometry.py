"""
CONCEPT: Math & Geometry

Soluții de referință — toate testele trec. Citește-le, apoi încearcă să le
rescrii din memorie fără să te uiți. Verifică astfel:

    python3 practice/24_math_geometry.py

Output: [v] test trecut, [x] test picat, la final N/M passed.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Happy Number  (LeetCode 202)
#
# A happy number is defined by the following process: starting with any
# positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle that does not include 1. Those
# numbers for which this process ends in 1 are happy. Return True if n is a
# happy number, and False if not.
#
# Example 1:
#   Input: n = 19
#   Output: True
#   Explanation: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100,
#   1^2 + 0^2 + 0^2 = 1, so 19 is happy.
# Example 2:
#   Input: n = 2
#   Output: False
#   Explanation: the process never reaches 1, it enters the cycle
#   4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4.
#
# Constraints:
#   - 1 <= n <= 2^31 - 1
#
# Hint: the repeated digit-square-sum is a function on the integers, so the
# question is cycle detection on a functional graph (Floyd or a seen set).
# ---------------------------------------------------------------------------
def p1_is_happy(n):
    # digit-square-sum is a function on the integers, so iterating it draws a
    # "rho": a tail that enters a cycle. Floyd's tortoise & hare detects the
    # meeting point with O(1) space, then the number is happy iff the cycle is
    # the fixed point 1.
    def step(x):
        total = 0
        while x:
            x, digit = divmod(x, 10)
            total += digit * digit
        return total

    slow = fast = n
    while True:
        slow = step(slow)
        fast = step(step(fast))
        if slow == fast:
            break
    return slow == 1


# ---------------------------------------------------------------------------
# Problem 2 - Pow(x, n)  (LeetCode 50)
#
# Implement fast exponentiation: return x raised to the integer power n,
# without using the built-in `**` on non-trivial exponents (fast
# exponentiation is exactly what the exercise is about). n may be negative.
#
# Note on comparison: the tests compare the float result with exact equality,
# which is only safe because every test value is exactly representable as a
# float (powers of 2, of 0.5 = 2^-1, and 1.0). Do not feed irrational or
# long-decimal inputs into an exact-equality check.
#
# Example 1:
#   Input: x = 2.0, n = 10
#   Output: 1024.0
# Example 2:
#   Input: x = 2.0, n = -2
#   Output: 0.25
#   Explanation: 2^-2 = 1 / 4 = 0.25.
#
# Constraints:
#   - -100 < x < 100
#   - -2^31 <= n <= 2^31 - 1
#   - n is an integer, and either x != 0 or n > 0
#
# Hint: x^n = (x^2)^(n/2) for even n, else x * x^(n-1). For a negative
# exponent use x^n = (1/x)^(-n); in Python negating -2^31 is safe (no 32-bit
# overflow), unlike in C++/Java.
# ---------------------------------------------------------------------------
def p2_my_pow(x, n):
    # Fast exponentiation: square the base and halve the exponent, and use
    # the current bit of n to decide whether the base enters the product.
    # x^(-n) == (1/x)^n, so a negative exponent only flips the base.
    if n < 0:
        x = 1.0 / x
        n = -n

    result = 1.0
    base = x
    while n:
        if n & 1:
            result *= base
        base *= base
        n >>= 1
    return result


# ---------------------------------------------------------------------------
# Problem 3 - Count Primes  (LeetCode 204)
#
# Given an integer n, return the number of prime numbers strictly less than
# n.
#
# Example 1:
#   Input: n = 10
#   Output: 4
#   Explanation: there are 4 primes less than 10: 2, 3, 5 and 7.
# Example 2:
#   Input: n = 0
#   Output: 0
#
# Constraints:
#   - 0 <= n <= 5 * 10^6
#
# Hint: sieve of Eratosthenes, O(n log log n). Cross out multiples of every
# prime p with p*p < n, then count the survivors.
# ---------------------------------------------------------------------------
def p3_count_primes(n):
    # Sieve of Eratosthenes, O(n log log n). A bytearray keeps 5 * 10^6 flags
    # at ~5 MB instead of ~40 MB for a list of Python bools.
    if n < 3:
        return 0
    sieve = bytearray(b"\x01") * n  # sieve[i] == 1 means "i is prime so far"
    sieve[0] = sieve[1] = 0
    p = 2
    while p * p < n:
        if sieve[p]:
            # p*p, p*p+p, ... are composite; the slice assignment is C-speed.
            sieve[p * p : n : p] = bytearray(len(range(p * p, n, p)))
        p += 1
    return sum(sieve)


if __name__ == "__main__":
    tests = [
        ("P1 is_happy", p1_is_happy, (19,), True),
        ("P1 is_happy example 2", p1_is_happy, (2,), False),
        ("P1 is_happy n = 1", p1_is_happy, (1,), True),
        ("P1 is_happy seven", p1_is_happy, (7,), True),
        ("P1 is_happy power of ten", p1_is_happy, (100,), True),
        ("P1 is_happy inside the cycle", p1_is_happy, (4,), False),
        ("P1 is_happy three digits", p1_is_happy, (999,), False),
        ("P2 my_pow", p2_my_pow, (2.0, 10), 1024.0),
        ("P2 my_pow negative exponent", p2_my_pow, (2.0, -2), 0.25),
        ("P2 my_pow exponent 0", p2_my_pow, (2.0, 0), 1.0),
        ("P2 my_pow fraction base", p2_my_pow, (0.5, 3), 0.125),
        ("P2 my_pow fraction base negative exponent", p2_my_pow, (0.5, -2), 4.0),
        ("P2 my_pow negative base odd exponent", p2_my_pow, (-2.0, 3), -8.0),
        ("P2 my_pow base 1", p2_my_pow, (1.0, -2147483648), 1.0),
        ("P2 my_pow base -1 max exponent", p2_my_pow, (-1.0, 2147483647), -1.0),
        ("P3 count_primes", p3_count_primes, (10,), 4),
        ("P3 count_primes n = 0", p3_count_primes, (0,), 0),
        ("P3 count_primes n = 1", p3_count_primes, (1,), 0),
        ("P3 count_primes n = 2", p3_count_primes, (2,), 0),
        ("P3 count_primes n = 3", p3_count_primes, (3,), 1),
        ("P3 count_primes up to 100", p3_count_primes, (100,), 25),
        ("P3 count_primes up to 1000", p3_count_primes, (1000,), 168),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
