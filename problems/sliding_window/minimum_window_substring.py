# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

def min_window_substring(s, t):
    if not s or not t:
        return ""

    t_dict = {}
    current_window_dict = {}

    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1
    
    left = 0
    min_len = float('inf')
    min_window = ""
    required_chars = len(t_dict)

    found_chars = 0

    for right in range(len(s)):
        char = s[right]

        current_window_dict[char] = current_window_dict.get(char, 0) + 1

        if char in t_dict and current_window_dict[char] == t_dict[char]:
            found_chars += 1

        while left <= right and found_chars == required_chars:
            window_size = right - left + 1

            if window_size < min_len:
                min_len = window_size
                min_window = s[left:right+1]
            
            left_char = s[left]
            current_window_dict[left_char] -= 1

            if left_char in t_dict and current_window_dict[left_char] < t_dict[left_char]:
                found_chars -= 1

            left += 1
    
    return min_window


# Example 1:
print(min_window_substring("ADOBECODEBANC", "ABC"))

# BANC
