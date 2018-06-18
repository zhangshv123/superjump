"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"].
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, 0, 4, 12, [], res)
        return res
        
    def dfs(self, s, start, minSize, maxSize, path, res):
        #cut branch, remaining size in range(minSize, maxSize)
        if len(s) - start >= minSize and len(s) - start <= maxSize:
            #base
            if minSize == 0:
                res.append(".".join(path))
            for i in range(start, len(s)):
                #"025"
                if i != start and s[start] == "0":
                    break
                #"552"
                if int(s[start: i + 1]) > 255:
                    break
                path.append(s[start: i + 1])
                self.dfs(s, i + 1, minSize - 1, maxSize - 3, path, res)
                path.pop()
               
"""
使用stack来做dfs，固定高度
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res, path, stk = [], ["" for i in range(4 + 1)], []
        stk.append(("", 0, 4, 12, 0))
        while len(stk) > 0:
            # print stk[-1], path, stk, res
            word, start, minSize, maxSize, height = stk.pop()
            if len(s) - start >= minSize and len(s) - start <= maxSize:
                path[height] = word
                #base
                if minSize == 0:
                    res.append(".".join(path[1:]))
                for i in range(start, len(s)):
                    #"025"
                    if i != start and s[start] == "0":
                        break
                    #"552"
                    if int(s[start: i + 1]) > 255:
                        break
                    stk.append((s[start: i + 1], i + 1, minSize - 1, maxSize - 3, height + 1))
        return res 


#使用stack来做dfs，不固定高度
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res, path, stk = [], [], []
        stk.append(("", 0, 4, 12, 0))
        while len(stk) > 0:
            # print stk[-1], path, stk, res
            word, start, minSize, maxSize, height = stk.pop()
            if len(s) - start >= minSize and len(s) - start <= maxSize:
                if len(path) <= height:
                    path.append(word)
                else:
                    path[height] = word
                #base
                if minSize == 0:
                    res.append(".".join(path[1:]))
                for i in range(start, len(s)):
                    #"025"
                    if i != start and s[start] == "0":
                        break
                    #"552"
                    if int(s[start: i + 1]) > 255:
                        break
                    stk.append((s[start: i + 1], i + 1, minSize - 1, maxSize - 3, height + 1))
        return res
from collections import deque
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res, q = [], deque()
        q.append(("", 0, 4, 12, 0))
        while len(q) > 0:
            ans, start, minSize, maxSize, height = q.popleft()
            if len(s) - start >= minSize and len(s) - start <= maxSize:
                #base
                if minSize == 0:
                    res.append(ans)
                for i in range(start, len(s)):
                    #"025"
                    if i != start and s[start] == "0":
                        break
                    #"552"
                    if int(s[start: i + 1]) > 255:
                        break
                    newAws = s[start: i + 1] if len(ans) == 0 else ans + "." + s[start: i + 1]
                    q.append((newAws, i + 1, minSize - 1, maxSize - 3, height + 1))
        return res        