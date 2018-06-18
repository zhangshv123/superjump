#!/usr/bin/python

class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses
    def isValidNum(self, s):
        if len(s) > 4 or len(s) == 0:
            return False
        if s != "0" and s.startswith("0"):
            return False
        if int(s) > 255:
            return False
        return True
    def restore_helper(self, s, step):
        res = []
        if step == 1:
            if self.isValidNum(s):
                return [s]
            else:
                return []
        for i in range(len(s)):
            if self.isValidNum(s[:i+1]):
                res += map(lambda c:s[:i+1] + "." + c, self.restore_helper(s[i+1:], step - 1))
        return res
                
    def restoreIpAddresses(self, s):
        # Write your code here
        return self.restore_helper(s, 4)
s = Solution()
print s.restoreIpAddresses("010010")