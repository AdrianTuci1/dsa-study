
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t)
            return False

        freq_map = {}
        for i in range(len(s))
            if s[i] in freq_map:
                freq_map[s[i]] +=1
            else:
                freq_map[s[i]] = 1

        if t[i] in freq_map:
            freq_map[t[i]] -= 1
        else:
            freq_map[t[i]] = -1

        for char in freq_map:
            if freq_map[char] != 0:
                return False
        
        return True


sol = Solution()

# Test case 1
s1 = "listen"
t1 = "silent"
print(sol.isAnagram(s1, t1))  # Expected output: True

# Test case 2
s2 = "hello"
t2 = "world"
print(sol.isAnagram(s2, t2))  # Expected output: False

# Test case 3
s3 = "anagram"
t3 = "nagaram"
print(sol.isAnagram(s3, t3))  # Expected output: True

# Test case 4
s4 = "rat"
t4 = "car"
print(sol.isAnagram(s4, t4))  # Expected output: False

# Test case 5
s5 = ""
t5 = ""
print(sol.isAnagram(s5, t5))  # Expected output: True