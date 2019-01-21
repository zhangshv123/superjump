题目：
      5
    /   \
   3     2
  / \     \
 2   4     4
            \
             1
自底向上的输出path [1,4,2,5] [2,3,5] [4,3,5],一定按Leaf的大小顺序输出
from collections import deque, defaultdict
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def lexiOrder(self, root):
		res = []
		self.dfs(root, res, root)
		return res
	
	def dfs(self, node, res, root):
		if not node.left and not node.right:
			return [[node.val]]
		
		if node.left:
			left = self.dfs(node.left, res, root)
		if node.right:
			right = self.dfs(node.right, res, root)
		
		for path in left:
			path.insert(0, node.val)
			if node == root:
				res.append(path)
		
		for path in right:
			path.insert(0, node.val)
			if node == root:
				res.append(path)
		return left + right
		
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
#root.right.left = TreeNode(6)
#root.right.right = TreeNode(7)

s = Solution()
print s.lexiOrder(root)
					
		