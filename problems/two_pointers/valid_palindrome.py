# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    s = s.lower()
    cleaned_s = ''.join(c for c in s if c.isalnum())
    left, right = 0, len(cleaned_s) - 1

    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False

        left += 1
        right -= 1

    return True


# Example 1:
input1 = "A man, a plan, a canal: Panama"
output1 = isPalindrome(input1)
print(output1)



