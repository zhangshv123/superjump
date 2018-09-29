思路：因为这里是找smallest，所以就用inorder，如果是找largest，就reverse inorder变成右根左
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution(object):
	def kthSmallest(self, root, k):
		count = [0]#不能用int
		res = [-1]#不能用int
		self.dfs(root, k, count, res)
		return res[0]
	
	def dfs(self, node, k, count, res):
		if node == None or count[0] >=k:
			return 
		
		self.dfs(node.left, k, count, res)
		count[0] += 1
		if count[0] == k:
			res[0] = node.val
		self.dfs(node.right, k, count, res)

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
#root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
#root.right.left = TreeNode(6)
#root.right.right = TreeNode(7)

s = Solution()
print s.kthSmallest(root,2)
		