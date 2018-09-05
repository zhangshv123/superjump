思路：每一个节点的左右子树的value序列化，存储在hashmap中，这样就是判断string有没有相同的
from collections import defaultdict
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def findDuplicateSubtrees(self, root):
		res = []
		d = defaultdict(int)
		self.serialize(root, d, res)
		return res
		
	
	def serialize(self, root, d, res):
		if not root:
			return "#"
		key = str(root.val) + "," + self.serialize(root.left, d, res) + self.serialize(root.right, d, res)
		d[key] += 1
		if d[key] == 2:
			res.append(root)
		return key
					
#root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.right.left = TreeNode(2)
#root.right.right = TreeNode(4)
#root.right.left.left = TreeNode(4)

root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(3)

s = Solution()
print s.findDuplicateSubtrees(root)		
		
			