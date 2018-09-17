给一个 二叉树 ， 求最深节点的最小公共父节点
		 1
	   2   3
		  5  6    return 3.

		 1  
	   2   3
   4      5 6   retrun 1. 
思路：
Recursion: 返回的时候返回lca和depth
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def deepestLowestCommonAncestor(self, root):
		return self.dfs(root)[1]
	
	def dfs(self, node):
		if not node:
			return (0, None)
				
		ldepth, lca = self.dfs(node.left)
		rdepth, rca = self.dfs(node.right)
		
		if ldepth == rdepth:
			return (ldepth+1, node.val)
		if ldepth > rdepth:
			return (ldepth+1, node.left.val)
		return (rdepth+1, node.right.val)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

s = Solution()
print s.deepestLowestCommonAncestor(root)