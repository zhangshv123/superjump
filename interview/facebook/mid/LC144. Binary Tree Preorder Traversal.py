迭代算法：
preOrder: 直接stack
inOrder: stack+cur
postOrder: stack+cur+prev
class Solution(object):
	def preorderTraversal(self, root):
		res = []
		if not root:
			return res
		stk = []
		stk.append(root)
		while len(stk) > 0:
			node = stk.pop()
			res.append(node.val)
			if node.right:
				stk.append(node.right)
			if node.left:
				stk.append(node.left)
		return res
				
			