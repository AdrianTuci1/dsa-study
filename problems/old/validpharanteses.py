# Determine if an input string containing only the characters '(', ')', '{', '}', '[', and ']' is valid. A string is considered valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Each close bracket has a corresponding open bracket of the same type.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}", "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

sol = Solution()
print(solution.isValid("(]"))
print(solution.isValid("{[]}"))

