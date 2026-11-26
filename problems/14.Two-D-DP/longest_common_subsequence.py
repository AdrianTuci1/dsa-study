# Problem Description
# You are given two strings text1 and text2. Your task is to find the length of their longest common subsequence.

# A subsequence is a sequence that can be derived from a string by deleting some characters (possibly none) without changing the order of the remaining characters. For example, "ace" is a subsequence of "abcde" because you can delete 'b' and 'd' while keeping the relative positions of 'a', 'c', and 'e'.

# A common subsequence is a subsequence that appears in both strings. The longest common subsequence is the common subsequence with the maximum possible length.

# The solution uses dynamic programming with a 2D table f[i][j] where each cell represents the length of the longest common subsequence between the first i characters of text1 and the first j characters of text2.

# The algorithm works by iterating through both strings and applying these rules:

# If characters at position i-1 in text1 and position j-1 in text2 match, we extend the previous longest common subsequence by 1: f[i][j] = f[i-1][j-1] + 1
# If characters don't match, we take the maximum of either excluding the current character from text1 or excluding it from text2: f[i][j] = max(f[i-1][j], f[i][j-1])
# The final answer is stored in f[m][n], where m and n are the lengths of text1 and text2 respectively.

# If no common subsequence exists, the function returns 0.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #get lengths of both strings
        len1, len2 = len(text1), len(text2)

        #initialize dp table with dimensions
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        #fill the dp table using bottom-up approach
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len1][len2]





