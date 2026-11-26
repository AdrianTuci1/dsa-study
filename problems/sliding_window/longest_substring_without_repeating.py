# Given a string s, find the length of the longest substring without repeating characters.

def length_of_longest_substring(s):
    char_index = {}

    start = 0
    max_length = 0

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1

    char_index[s[end]] = end

    current_length = end - start + 1
    max_length = max(max_length, current_length)

    return max_length


# Example 1:
print(length_of_longest_substring("abcabcbb"))
# 3
