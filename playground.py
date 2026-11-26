# ---------------------------------------------------------------------------
# Problem 1 - Two Sum  (LeetCode 1)
#
# Given a list of integers `nums` and an integer `target`, return the indices
# of the two numbers that add up to `target` as a list [i, j] with i < j.
# Assume that every input has exactly one valid answer, and the same element
# may not be used twice. Using a hash map lets you solve it in one pass.
#
# Example 1:
#   Input: nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]
#   Explanation: because nums[0] + nums[1] == 9
# Example 2:
#   Input: nums = [3, 2, 4], target = 6
#   Output: [1, 2]
#
# Constraints:
#   - 2 <= len(nums) <= 10^4
#   - exactly one valid answer exists
# ---------------------------------------------------------------------------

def p1_two_sum(nums, target):
    seen = {} #initiem seen
    for i, x in enumerate(nums): #iteram prin nums
        need = target - x #scazi un dict din int
        if need in seen: #daca numarul pe care il vrem se afla in vazute
            return [seen[need], i] #returnam indecsii celor 2 numere
        seen[x] = i #altfel valoarea lui seen este egala cu indexul
    return []


def p2_is_anagram(s, t):
    if len(s) != len(t): #daca lungimile nu sunt egale returnam False
        return False
    
    counts = {} #caracter > numar de aparitii
    for char in s: #iteram fiecare char din primul sir
        counts[char] = counts.get(char, 0) + 1 #crestem frecventa caracterului
    
    for char in t: #iteram fiecare char din al 2-lea sir
        if char not in counts: #daca un caracter nu se gaseste in counts
            return False 
        counts[char] -= 1 #scadem din stocul de aparitii ramase
        if counts[char] < 0: #am consumat mai multe aparitii decat exista in s
            return False
    return True #altfel e anagrama



def p3_longest_consecutive(nums):
    present = set(nums) #initiem un sir
    longest = 0

    for n in present: #pentru fiecare numar din sir
        if n - 1 not in present: #daca valoarea lui -1 nu e in sir
            length = 1 #lungimea e 1
            while n + length in present: # cat timp numarul + 1 e prezent
                length += 1 #lungimea creste cu 1
            longest = max(longest, length) #longest e implicit lungimea gasita, doar pastram variabila si o actualizam 
    
    return longest



def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True




def longest_ones(nums, k):
    left = 0
    zeros = 0
    best = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best