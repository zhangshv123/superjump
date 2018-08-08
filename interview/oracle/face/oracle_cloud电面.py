# binary tree, 0, 1. remove the subtrees that only contains 0. 
#   0 -> null 
# . 0         0
# 0  0 ->  None
#
#    1
#  0 . 0
# 1 0 
def findSubtree(root):
	if root == None:
		return None
	helper(root)
	return root

def helper(node):
	if node.left == None and node.right == None and node.val == 0:
		return False
	
	if node.left:
		left = helper(node.left)
	if node.right:
		right = helper(node.right)
	
	if not left:
		node.left = None
	if not right:
		node.right = None
	return left or right or root.val == 1
