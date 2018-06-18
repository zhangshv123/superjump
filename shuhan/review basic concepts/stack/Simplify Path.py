#!/usr/bin/python

class Solution:
    # @param {string} path the original path
    # @return {string} the simplified path
    def simplifyPath(self, path):
        # Write your code here
        strs = path.split("/")
        stk =[]
        for str in strs:
            if str in [".", ""]:
                continue
            elif ".." == str:
                if len(stk) >0:
                    stk.pop()
            else:
                stk.append(str)
        return "/" + "/".join(stk)
s = Solution()
print s.simplifyPath("/home/foo")
                
                
        