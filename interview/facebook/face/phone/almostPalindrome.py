"""
A string S is an 'almost palindrome' if you can remove 0 or 1 character from S to make a palindrome.. 鍥磋鎴戜滑@1point 3 acres
e.g. momo
Given a string S determine if it is an almost palindrome. 
"""
#!/usr/bin/python
class Solution(object):
    def almostPalindrome(self, s):
        i, j = 0, len(s) - 1
        count = 0
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(i, j - 1) or isPalindrome(i + 1, j)
            i += 1
            j -= 1
        return True
s = Solution()
print(s.almostPalindrome("abccffa"))