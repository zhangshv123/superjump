"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if len(nums) == 0:
            return res
        prev = 0
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i - 1] != nums[i] - 1:
                if prev != i-1:
                    res.append(str(nums[prev]) + "->" + str(nums[i-1]))
                else:
                    res.append(str(nums[prev]))
                prev = i
        return res
        
        