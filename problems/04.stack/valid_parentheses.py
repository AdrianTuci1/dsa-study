# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def isValid(s):
    #create empty stack to store opening brackets
    stack = []

    bracket_mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        #if opening bracket push into stack
        if char in bracket_mapping.values():
            stack.append(char)
        #if closing bracket
        elif char in bracket_mapping.keys():
            #pop the top element from the stack if it exists, or use a dummy value
            top_element = stack.pop() if stack else '#'
            #if popped element does not match the corresponding opening bracket, return False
            if bracket_mapping[char] != top_element:
                return False
            #if character not a bracket, ignore it
    
    #if there are any unmatched opening brackets in the stack, return False
    return len(stack) == 0


# Example 1:
print(isValid("()"))    
# True