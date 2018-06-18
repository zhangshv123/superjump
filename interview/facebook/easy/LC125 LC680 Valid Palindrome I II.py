"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = filter(lambda a:a.isalnum(), s).lower()
        l, r = 0, len(a) - 1
        while l < r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True

# II you may delete at most one character. Judge whether you can make it a palindrome.
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(l, r):
            while l < r:
                if a[l] != a[r]:
                    return False
                l += 1
                r -= 1
            return True
        a = filter(lambda a:a.isalnum(), s).lower()
        l, r = 0, len(a) - 1
        while l < r:
            if a[l] != a[r]:
                return isPalindrome(l, r - 1) or isPalindrome(l + 1, r)
            l += 1
            r -= 1
        return True
