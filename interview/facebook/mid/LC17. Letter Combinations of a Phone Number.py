"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
"""
iteration
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) == 0:
            return []
        d = {    '2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']
                    }
        res = ['']
        for digit in digits:
            new_res = []
            for c in d[digit]:
                for aws in res:
                    new_res.append(aws + c)
            res = new_res
        return res
"""
recursion
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {    '2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']
                    }
        res = []
        if len(digits) == 0:
            return res
        self.dfs(0, "", res, digits, d)
        return res
        
    def dfs(self, index, path, res, digits, d):
        #base
        if index == len(digits):
            return res.append(path)
        #recursion
        for char in d[digits[index]]:
            self.dfs(index + 1, path + char, res, digits, d)