# 和 lc257 一模一样！
class Solution(object):
	def sumNumbers(self, root):
		if not root:
			return 0
		self.dfs(root)
		total = 0
		res = self.dfs(root)
		for path in res:
			total += int("".join(path))
		
		return total
	
	def dfs(self, node):
		if not node.left and not node.right:
			return [[str(node.val)]]
		
		left_path, right_path = [], []
		if node.left:
			left_path = self.dfs(node.left)
		if node.right:
			right_path = self.dfs(node.right)
		
		for path in left_path:
			path.insert(0, str(node.val))
		
		for path in right_path:
			path.insert(0, str(node.val))
		
		return left_path + right_path
		