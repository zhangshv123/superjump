class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def binaryTreePaths(self, root):
		new_res = []
		if not root:
			return new_res
		res = self.dfs(root)
		for path in res:
			new_path = "->".join(path)
			new_res.append(new_path)
		return new_res
		
	dfs的定义： 
	叶子节点返回[[node.val]]
	非叶子节点就是node接上所有的left和right的节点
	def dfs(self, node):
		if not node.left and not node.right:
			return [[str(node.val)]]
			
		res = []
		if node.left:
			left = self.dfs(node.left)
			for path in left:
				path.insert(0,str(node.val))
				res.append(path)
		if node.right:
			right = self.dfs(node.right)
			for path in right:
				path.insert(0,str(node.val))
				res.append(path)
		return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

s = Solution()
print s.binaryTreePaths(root) 

