# 更容易理解的版本！自己写出来的，太开心了！

import sys
class Solution(object):
    def maxPathSum(self, root):
        if not root:
            return -sys.maxint
            
        leftSingle = self.getSinglePath(root.left)
        rightSingle = self.getSinglePath(root.right)
        
        pathSum = leftSingle + rightSingle + root.val
        
        
        return max(self.maxPathSum(root.left), self.maxPathSum(root.right), pathSum)
    
    def getSinglePath(self, node):
        if not node:
            return 0
        if not node.left and not node.right and node.val > 0:
            return node.val
        
        left = self.getSinglePath(node.left)
        right = self.getSinglePath(node.right)
        
        bigger = max(left, right)
        
        return max(0, node.val + bigger)



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