"""
STRUCTURA: STACK (stivă)

Ce este:
    Structură LIFO (Last In, First Out) — ultimul intrat e primul ieșit.
    Gândește „teanc de farfurii": pui deasupra, iei de deasupra.

Operații și complexitate:
    push(x)   O(1)
    pop()     O(1)
    peek()    O(1)
    is_empty  O(1)

Ideea-cheie:
    Folosită când trebuie să memorezi „context" într-o ordine inversă:
    paranteze valide, evaluare de expresii, DFS iterativ, monotonic stack.

Notă: aici implementăm de la zero. În cod real, stiva e pur și simplu o listă
Python (`append` / `pop`) sau `collections.deque`.
"""


class Stack:
    def __init__(self, iterable=None):
        self._data = list(iterable) if iterable else []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return not self._data

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack(bottom -> top: {self._data})"


def is_valid_parentheses(s):
    """Aplicație clasică: parantezele sunt echilibrate? O(n)."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    for ch in s:
        if ch in pairs:
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
        else:
            stack.push(ch)
    return stack.is_empty()


if __name__ == "__main__":
    st = Stack()
    for x in [1, 2, 3]:
        st.push(x)
    print(st)                       # bottom -> top: [1, 2, 3]
    print("peek ->", st.peek())     # 3
    print("pop  ->", st.pop())      # 3
    print("dupa pop:", st)          # [1, 2]

    print('is_valid("()[]{}") ->', is_valid_parentheses("()[]{}"))   # True
    print('is_valid("(]")     ->', is_valid_parentheses("(]"))       # False
