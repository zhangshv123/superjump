"""
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""
class Solution(object):
    def group(self, start, end):
        if start + 2 == end:
            return str(start + 1)
        else:
            return str(start + 1) + "->" + str(end - 1)
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        for i in range(len(nums) + 1):
            start = lower - 1 if i == 0 else nums[i - 1]
            end = upper + 1 if i == len(nums) else nums[i]
            if start + 1 < end:
                res.append(self.group(start, end))
        return res
            