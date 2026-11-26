"""
CONCEPT: Matrix / 2D Grid

Soluții de referință — toate testele trec. Citește-le, apoi încearcă să le
rescrii din memorie fără să te uiți. Verifică astfel:

    python3 practice/22_matrix.py

Output: [v] test trecut, [x] test picat, la final N/M passed.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Spiral Matrix  (LeetCode 54)
#
# Given an m x n matrix `matrix`, return a single list with all elements of
# the matrix in spiral order, starting from the top-left corner and moving
# right, then down, then left, then up, and so on inwards. The matrix is not
# modified. An empty matrix has an empty spiral.
#
# Example 1:
#   Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
# Example 2:
#   Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#   Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
#
# Constraints:
#   - 0 <= m, n <= 10
#   - -100 <= matrix[i][j] <= 100
# ---------------------------------------------------------------------------
def p1_spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    # Keep four walls and peel one layer at a time. After the top row and the
    # right column, re-check the walls: the layer may already be exhausted.
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    out = []
    while top <= bottom and left <= right:
        for c in range(left, right + 1):          # left -> right
            out.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):          # top -> bottom
            out.append(matrix[r][right])
        right -= 1
        if top <= bottom:                         # bottom -> left
            for c in range(right, left - 1, -1):
                out.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:                         # bottom -> top
            for r in range(bottom, top - 1, -1):
                out.append(matrix[r][left])
            left += 1
    return out


# ---------------------------------------------------------------------------
# Problem 2 - Rotate Image  (LeetCode 48)
#
# Given an n x n matrix `matrix`, rotate it 90 degrees clockwise. The
# rotation must happen IN PLACE: mutate `matrix` itself and do not build a
# new matrix. Do not return anything (returning None is fine).
#
# Because the result is in the mutated argument, the tests below call the
# helper `_rotated(matrix)`, defined after the solutions: it copies the input,
# calls p2_rotate on the copy and compares the mutated copy. Write your
# function so that `_rotated` sees the rotated matrix.
#
# Example 1:
#   Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# Example 2:
#   Input: matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
#   Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
#
# Constraints:
#   - 1 <= n <= 20
#   - matrix is square: len(matrix) == len(matrix[i])
#   - -1000 <= matrix[i][j] <= 1000
# ---------------------------------------------------------------------------
def p2_rotate(matrix):
    # 90 degrees clockwise == transpose, then reverse every row.
    # `matrix[:] = ...` replaces the contents in place, which is what the
    # "in place" requirement asks for: the caller's list is the same object.
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]


# ---------------------------------------------------------------------------
# Problem 3 - Set Matrix Zeroes  (LeetCode 73)
#
# Given an m x n matrix `matrix`, if an element is 0, set its entire row and
# its entire column to 0. The change must happen IN PLACE: mutate `matrix`
# itself. Do not return anything (returning None is fine).
#
# As above, the tests call the helper `_zeroed(matrix)`, defined after the
# solutions: it copies the input, calls p3_set_zeroes on the copy and compares
# the mutated copy.
#
# Example 1:
#   Input: matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
#   Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
# Example 2:
#   Input: matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
#   Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
#
# Constraints:
#   - 0 <= m, n <= 200
#   - -2^31 <= matrix[i][j] <= 2^31 - 1
# ---------------------------------------------------------------------------
def p3_set_zeroes(matrix):
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])
    # Use the first row and first column as marker arrays (O(1) extra space).
    # Remember separately whether they themselves must become zero, because
    # writing markers there would destroy their original values.
    first_row_zero = any(matrix[0][c] == 0 for c in range(n))
    first_col_zero = any(matrix[r][0] == 0 for r in range(m))

    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if first_row_zero:
        for c in range(n):
            matrix[0][c] = 0
    if first_col_zero:
        for r in range(m):
            matrix[r][0] = 0


def _rotated(matrix):
    """Copy `matrix`, rotate the copy in place with p2_rotate, return it."""
    grid = [row[:] for row in matrix]
    p2_rotate(grid)
    return grid


def _zeroed(matrix):
    """Copy `matrix`, zero the copy in place with p3_set_zeroes, return it."""
    grid = [row[:] for row in matrix]
    p3_set_zeroes(grid)
    return grid


if __name__ == "__main__":
    tests = [
        ("P1 spiral_order", p1_spiral_order, ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
         [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ("P1 spiral_order", p1_spiral_order,
         ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ("P1 spiral_order empty", p1_spiral_order, ([],), []),
        ("P1 spiral_order 1x1", p1_spiral_order, ([[1]],), [1]),
        ("P1 spiral_order single row", p1_spiral_order, ([[1, 2]],), [1, 2]),
        ("P1 spiral_order single column", p1_spiral_order, ([[1], [2], [3]],), [1, 2, 3]),
        ("P1 spiral_order all zeros", p1_spiral_order, ([[0, 0], [0, 0]],), [0, 0, 0, 0]),
        ("P1 spiral_order negatives", p1_spiral_order, ([[-1, -2], [-3, -4]],), [-1, -2, -4, -3]),
        ("P2 rotate", _rotated,
         ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ("P2 rotate", _rotated,
         ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],),
         [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
        ("P2 rotate 1x1", _rotated, ([[1]],), [[1]]),
        ("P2 rotate 2x2", _rotated, ([[1, 2], [3, 4]],), [[3, 1], [4, 2]]),
        ("P2 rotate all zeros", _rotated, ([[0, 0], [0, 0]],), [[0, 0], [0, 0]]),
        ("P2 rotate negatives", _rotated, ([[-1, -2], [-3, -4]],), [[-3, -1], [-4, -2]]),
        ("P2 rotate 5x5", _rotated,
         ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],),
         [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3],
          [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]),
        ("P3 set_zeroes", _zeroed,
         ([[1, 1, 1], [1, 0, 1], [1, 1, 1]],), [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ("P3 set_zeroes", _zeroed, ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],),
         [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
        ("P3 set_zeroes empty", _zeroed, ([],), []),
        ("P3 set_zeroes 1x1", _zeroed, ([[1]],), [[1]]),
        ("P3 set_zeroes single zero", _zeroed, ([[0]],), [[0]]),
        ("P3 set_zeroes no zeros", _zeroed, ([[1, 1], [1, 1]],), [[1, 1], [1, 1]]),
        ("P3 set_zeroes all zeros", _zeroed, ([[0, 0], [0, 0]],), [[0, 0], [0, 0]]),
        ("P3 set_zeroes diagonal", _zeroed, ([[1, 0], [0, 1]],), [[0, 0], [0, 0]]),
        ("P3 set_zeroes single row", _zeroed, ([[1, 0, 2]],), [[0, 0, 0]]),
        ("P3 set_zeroes single column", _zeroed, ([[1], [0], [2]],), [[0], [0], [0]]),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
