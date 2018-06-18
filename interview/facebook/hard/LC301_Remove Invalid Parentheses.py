"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            stk = []
            for c in s:
                if c == "(":
                    stk.append(c)
                if c == ")":
                    if len(stk) == 0:
                        return False
                    stk.pop()
            return len(stk) == 0
        visited = set()
        q = {s}
        while True:
            valids = list(filter(lambda a: isValid(a), q))
            if len(valids) > 0:
                return valids
            nq = set()
            for s in q:
                for i in range(len(s)):
                    cur = s[:i] + s[i + 1:]
                    nq.add(cur)
            q = nq

# 时间复杂度：2的N次方（worst case = big O）
from collections import deque
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if self.isValid(s):#一个都不删，需要特别对待
            return [s]
        q,sb= deque(),set()
        res = []
        q.append(s)
        while len(q) > 0:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                for j in range(len(cur)):
                    child = cur[:j]+cur[j+1:]
                    if child not in sb:
                        sb.add(child)
                        q.append(child)
                        if self.isValid(child):
                            res.append(child)
                    else:
                        continue   
            if len(res) > 0:
                return res
        return [""]
    
    def isValid(self,s):
        m = {"(":")","[":"]","{":"}"}
        stk = []
        for c in s:
            if c in m.keys():
                stk.append(c)
            elif c in m.values():
                if len(stk) == 0 or c != m[stk.pop()]:
                    return False
        return len(stk) == 0
            
s = Solution()
print s.removeInvalidParentheses("()())())")