"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 基础班视频 3._Binary_Tree__Divide_Conquer__DFS__BFS_part 2 6分钟
class Solution(object):
    #singlePath: 从root往下走的到任意一点的最大路径，这条路径可以不包含任何点,但如果包含一定包含root
    #maxPath: 从树中任意点到任意点的最大路径，这条路径至少包含一个点 
    def maxSumToRootAndPathSum(self, root):
        if root is None:
            return (0, -sys.maxint)
        leftSumToRoot, leftPathSum = self.maxSumToRootAndPathSum(root.left)
        rightSumToRoot, rightPathSum = self.maxSumToRootAndPathSum(root.right)
        sumToRoot = max(0, max(leftSumToRoot, rightSumToRoot) + root.val)
        pathSum = max(leftPathSum, rightPathSum, leftSumToRoot + root.val + rightSumToRoot)
        return (sumToRoot, pathSum)
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxSumToRootAndPathSum(root)[1]