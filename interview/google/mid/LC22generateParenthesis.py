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
    def generateParenthesis(self, n):
        left, right = n, n
        res = []
        self.dfs(n, n, [], res)
        return res
    
    def dfs(self, left, right, path, res):
        if left == 0 and right == 0:
            res.append("".join(path[:]))
            return
        
        if left > 0:
            path.append("(")
            self.dfs(left-1, right, path, res)
            path.pop()
        
        if right > left:
            path.append(")")
            self.dfs(left, right-1, path, res)
            path.pop()

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
