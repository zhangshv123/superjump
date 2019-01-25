思路：
https://blog.csdn.net/fuxuemingzhu/article/details/80781666
1.假如左子树高度等于右子树高度，则右子树为完全二叉树，左子树为满二叉树。
2.假如高度不等，则左字数为完全二叉树，右子树为满二叉树。
3.求高度的时候只往左子树来找。
class Solution(object):
	def countNodes(self, root):
		nodes = 0
		if not root:
			return nodes
		leftHeight, rightHeight = self.getHeight(root.left), self.getHeight(root.right)
		if leftHeight == rightHeight:
			nodes = 2**leftHeight + self.countNodes(root.right)
		else:
			nodes = 2**rightHeight + self.countNodes(root.left)
		return nodes
	
	def getHeight(self, node):
		height = 0
		while node:
			height += 1
			node = node.left
		return height