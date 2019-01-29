参考：
https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def diameter(self, root):
		if not root:
			return 0
		
		leftH, rightH = self.getHeight(root.left), self.getHeight(root.right)
		leftD, rightD = self.diameter(root.left), self.diameter(root.right)
		
		return max(leftH+rightH+1, leftD, rightD)
		
	
	def getHeight(self, node):
		if not node:
			return 0
		
		leftH = self.getHeight(node.left)
		rightH = self.getHeight(node.right)
		
		return 1 + max(leftH, rightH)
		
						
					
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)


s = Solution()
print s.diameter(root)