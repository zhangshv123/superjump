
和 path II 更像的版本，更好理解：
class Solution(object):
    def hasPathSum(self, root, curSum):
        res = []
        if not root:
            return False
        return self.dfs(root, curSum - root.val)
        
    def dfs(self, node, curSum):
        if not node.left and not node.right and curSum == 0:
            return True
        
        left, right = False, False
        if node.left:
            left = self.dfs(node.left, curSum-node.left.val)
            
        if node.right:
            right = self.dfs(node.right, curSum-node.right.val)
        
        return left or right



class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left == None and root.right == None and root.val == sum:
            return True
        
        return self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum - root.val)