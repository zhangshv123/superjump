class Solution(object):
    def minDis(self, nums):
        dis = 0
        for i in range(len(nums) / 2):
            dis += nums[len(nums) - 1 - i] - nums[i]
        return dis
    
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        numsX, numsY = [], [] 
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1:
                    numsX.append(i)
                    numsY.append(j)
        return self.minDis(sorted(numsX)) + self.minDis(sorted(numsY))