
"""
I
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
 the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
  it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of 
money you can rob tonight without alerting the police.

f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
"""

class Solution(object):
  def rob(self, nums):
    if len(nums) == 0 or not nums:
      return 0
    n = len(nums)
    if n == 1:
      return nums[0]
    elif n == 2:
      return max(nums[0], nums[1])
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2,n):
      dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[-1]



"""
II
all houses at this place are arranged in a circle. 

However, since we already have a nice solution to the simpler problem. We do not want to throw it away. 
Then, it becomes how can we reduce this problem to the simpler one. Actually, extending from the logic 
that if house i is not robbed, then you are free to choose whether to rob house i + 1, you can break 
the circle by assuming a house is not robbed.

For example, 1 -> 2 -> 3 -> 1 becomes 2 -> 3 if 1 is not robbed.

Since every house is either robbed or not robbed and at least half of the houses are not robbed, the 
solution is simply the larger of two cases with consecutive houses, i.e. house i not robbed, break 
the circle, solve it, or house i + 1 not robbed. Hence, the following solution. I chose i = n and 
i + 1 = 0 for simpler coding. But, you can choose whichever two consecutive ones.
"""

class Solution(object):
	def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    	if nums.length == 1
    		return nums[0]
    	return max(rob(nums[0: -1]), rob(nums[1:])


""" 
The thief has found himself a new place for his thievery again. There is only one entrance to this area, 
called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart 
thief realized that "all houses in this place forms a binary tree". It will automatically contact the police
if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
"""
dfs all the nodes of the tree, each node return two number, int[] num, num[0] is the max value while rob this node, 
num[1] is max value while not rob this value. Current node return value only depend on its children’s value. 
Transform function should be very easy to understand.
"""
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def supperrob(root):
            if root == None:
                return (0, 0)
            left, right = supperrob(root.left), supperrob(root.right)
            withRoot, withoutRoot = 0, 0
            withRoot = root.val + left[1] + right[1]
            withoutRoot = max(left) + max(right)
            return (withRoot, withoutRoot)
        return max(supperrob(root))








