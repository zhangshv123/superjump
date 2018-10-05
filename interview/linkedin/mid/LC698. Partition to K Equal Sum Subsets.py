"""
This question has been changed after the contest. It added the special restriction 0 < nums[i] < 10000. My solution here is without that consideration.

Assume sum is the sum of nums[] . The dfs process is to find a subset of nums[] which sum equals to sum/k. We use an array visited[] to record which element in nums[] is used. Each time when we get a cur_sum = sum/k, we will start from position 0 in nums[] to look up the elements that are not used yet and find another cur_sum = sum/k.

An corner case is when sum = 0, my method is to use cur_num to record the number of elements in the current subset. Only if cur_sum = sum/k && cur_num >0, we can start another look up process.

Some test cases may need to be added in:
nums = {-1,1,0,0}, k = 4
nums = {-1,1}, k = 1
nums = {-1,1}, k = 2
nums = {-1,1,0}, k = 2
时间复杂度： K的N次方
最终每个物品都有可能放在任何一个篮子里(k个)
空间复杂度：
O（N）
"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        tot = sum(nums)
        if k <= 0 or tot%k != 0 or len(nums) < k:
            return False
        visited = [0]*len(nums)
        return self.helper(nums,visited,0,k,0,0,tot/k)
    
    def helper(self,nums,visited,start,k,cur_sum,cur_num,target):
        if k == 1:
            return True
        if cur_sum == target and cur_num > 0:
            return self.helper(nums,visited,0,k-1,0,0,target)
        for i in range(start,len(nums)):
            if visited[i] == 0:
                visited[i] = 1
                if self.helper(nums,visited,i+1,k,cur_sum+nums[i],cur_num+1,target):
                    return True
                visited[i] = 0
        return False

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False
        target = total/k
        sumArr = [0 for i in range(k)]
        full = set()
        return self.dfs(nums, k, target, sumArr, 0)
    
    # return true if exists 
    def dfs(self, nums, k, target, sumArr, idx):
        if idx == len(nums):
            return True
        for i in range(k):
            if sumArr[i] + nums[idx] > target:
                continue
            sumArr[i] += nums[idx]
            if self.dfs(nums, k, target, sumArr, idx+1):
                return True
            sumArr[i] -= nums[idx]
        return False


s = Solution()
print s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)



