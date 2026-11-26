# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

def characterReplacement(s, k):
    max_length = 0
    max_count = 0
    start = 0
    char_count = {}

    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1

        max_count = max(max_count, char_count[s[end]])

        if (end - start + 1) - max_count > k:
            char_count[s[start]] -= 1
            start += 1
        
        max_length = max(max_length, end - start + 1)
    
    return max_length


# Example 1:
s1 = "ABAB"
k1 = 2
print(characterReplacement(s1, k1))

# 4