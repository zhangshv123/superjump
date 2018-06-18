"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def comp(self, a, b):
        m, n = a + b, b + a 
        for i in range(len(a) + len(b)):
            if m[i] != n[i]:
                return ord(n[i]) - ord(m[i])
        return 0
    def largestNumber(self, nums):
        strs = map(lambda a: str(a), nums)
        strs.sort(lambda a,b: self.comp(a, b))
        res = "".join(strs)
        return res if res[0] != "0" else "0"