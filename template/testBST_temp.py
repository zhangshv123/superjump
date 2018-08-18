# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		stk = []
		stk.append([root, False, False, None, None])
		while len(stk) > 0:
			curr = stk[-1]
			if curr[0]== p or curr[0] == q or not curr[0]:
				ret = curr[0]
				stk.pop()
				if len(stk)>0:
					if not stk[-1][1]:
						stk[-1][1] = True
					else:
						stk[-1][2] = True                
				continue
			if not curr[1]:
				stk.append([curr[0].left, False, False, None, None])
			elif not curr[2]:
				curr[3] = ret
				stk.append([curr[0].right, False, False, None, None])
			else:
				curr[4] = ret
				left, right = curr[3], curr[4]
				if left and right:
					ret = curr[0]
				elif not left and right:
					ret = right
				else:
					ret = left
				stk.pop()
				if len(stk)>0:
					if not stk[-1][1]:
						stk[-1][1] = True
					else:
						stk[-1][2] = True
		return ret

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
#root.right.left = TreeNode(6)
#root.right.right = TreeNode(7)

s = Solution()
print s.lowestCommonAncestor(root, root.right, root.left.left)        
