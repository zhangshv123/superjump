"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
#这种是top down recursion的，因为path所以空间复杂度较高，好写，但是不是最优解
class Solution(object):
    def traverse(self, lnum, rnum, n, path, res):
        #base
        if lnum + rnum == 2 * n:
            res.append(path)
            
        if lnum < n:
            self.traverse(lnum + 1, rnum, n, path + "(", res)
        if rnum < lnum:
            self.traverse(lnum, rnum + 1, n, path + ")", res)
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.traverse(0, 0, n, "", res)
        return res

#用stack来做dfs
class Solution(object):     
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res, stk, path = [], [], ["" for _ in range(2 * n + 1)]
        stk.append((0, 0, ""))
        while len(stk) > 0:
            lnum, rnum, c = stk.pop()
            path[lnum + rnum] = c
            #base
            if lnum + rnum == 2 * n:
                res.append("".join(path[1:]))
            if rnum < lnum:
                stk.append((lnum, rnum + 1, ")"))
            if lnum < n:
                 stk.append((lnum + 1, rnum, "("))
        return res

#用bfs来做
from collections import deque
class Solution(object): 
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res, q = [], deque()
        q.append((0, 0, ""))
        while len(q) > 0:
            lnum, rnum, s = q.popleft()
            #base
            if lnum + rnum == 2 * n:
                res.append(s)
            if rnum < lnum:
                q.append((lnum, rnum + 1, s + ")"))
            if lnum < n:
                q.append((lnum + 1, rnum, s + "("))
        return res        
