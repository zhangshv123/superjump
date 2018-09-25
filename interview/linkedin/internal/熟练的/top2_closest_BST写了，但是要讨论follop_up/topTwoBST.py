思路：
如果current.val == target， 那么top2就是左边最大或者右边最小
如果 current.val > target, 那么top2就是右边最小的或者是左边的某一个node
如果current.val < target, 那么top2就是左边最大的或者是右边的某一个node
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
import sys
class Solution(object):
	def topTwoClosestBST(self, root, target):
		arr = [sys.maxint, sys.maxint]
		while root:
			self.update(arr, root.val, target) #因为每一步操作都需要做，所以就放在最前面了
			if root.val == target:
				leftVal = self.findBiggest(root.left) #找左边最大
				rightVal = self.findSmallest(root.right)
				self.update(arr, leftVal, target)
				self.update(arr, rightVal, target)
			elif root.val > target:
				rightVal = self.findSmallest(root.right) #找右边最小
				self.update(arr, rightVal, target)
				root = root.left
			else:
				leftVal = self.findBiggest(root.left)
				self.update(arr, leftVal, target)
			 	root = root.right
		return arr
			
	def findSmallest(self, root):
		res = 0
		while root:
			res = root.val
			root = root.left
		return res
	
	def findBiggest(self, root):
		res = 0
		while root:
			res = root.val
			root = root.right
		return res
	
	def update(self, arr, val, target):
		if abs(arr[0] - target) > abs(val - target):
			arr[1]= arr[0]
			arr[0] = val
		elif abs(arr[1] - target) > abs(val - target):
			arr[1] = val
		return
root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(2)
root.right.left = TreeNode(14)
root.right.right = TreeNode(18)
root.right.right.left = TreeNode(17)


s = Solution()
print s.topTwoClosestBST(root, 17.9) 