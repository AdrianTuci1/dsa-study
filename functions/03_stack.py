"""
STACK — funcții (fără OOP)

Un stack e pur și simplu o listă Python folosită corect: adaugi/scoți doar la
un capăt (dreapta). Toate operațiile O(1).

Funcțiile primesc lista ca argument — nu există clasă.
"""


def new_stack(iterable=None):
    return list(iterable) if iterable else []


def push(stack, value):
    stack.append(value)


def pop(stack):
    if not stack:
        raise IndexError("pop from empty stack")
    return stack.pop()


def peek(stack):
    if not stack:
        raise IndexError("peek from empty stack")
    return stack[-1]


def is_empty(stack):
    return not stack


def size(stack):
    return len(stack)


def is_valid_parentheses(s):
    """Parantezele sunt echilibrate? O(n) cu stack."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = new_stack()
    for ch in s:
        if ch in pairs:
            if not stack or pop(stack) != pairs[ch]:
                return False
        else:
            push(stack, ch)
    return not stack


def next_greater(nums):
    """Pentru fiecare element, următorul mai mare din dreapta (-1 dacă nu e). O(n).

    Monotonic stack — scade din stivă tot ce e mai mic decât elementul curent.
    """
    result = [-1] * len(nums)
    stack = []               # ținem indici, cu valorile descrescătoare
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            result[stack.pop()] = x
        stack.append(i)
    return result


if __name__ == "__main__":
    st = new_stack()
    for x in [1, 2, 3]:
        push(st, x)
    print("stack:", st)                          # [1, 2, 3]
    print("peek ->", peek(st))                   # 3
    print("pop  ->", pop(st))                    # 3
    print("dupa pop:", st)                       # [1, 2]

    print('is_valid("()[]{}") ->', is_valid_parentheses("()[]{}"))  # True
    print('is_valid("(]")     ->', is_valid_parentheses("(]"))      # False

    print("next_greater:", next_greater([2, 1, 2, 4, 3]))  # [4, 2, 4, -1, -1]
