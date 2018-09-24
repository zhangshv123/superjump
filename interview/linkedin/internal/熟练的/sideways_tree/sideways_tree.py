def reverse(root):
	if not root.left and not root.right:
		return root
	nodeLeft = root.left
	nodeRight = root.right
	root.left = None
	root.right = None
	return helper(nodeLeft, root, nodeRight)
	

def help(node, top, right):
	nodeLeft = node.left
	nodeRight = node.right
	node.right = top
	node.left = right
	if nodeLeft == None:
		return node
	return help(nodeLeft, node, nodeRight)
	
	