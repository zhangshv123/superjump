# binary tree, 所有节点的value 只有 0 或者 1. 
#remove the subtrees that only contains 0. 
#   0 -> null 
# . 0         
#  0  0 ->  None
#
#    1   ->  1
#  0 . 0   0   
# 1 0    1  0
def findSubtree(root):
    if root.val == 0 or root == None:
        return None
    helper(root)
    return root

def helper(node): #if subtree of node only contains 0, return true
    if node.left == None and node.right == None and node.val == 0:
        return True
    
    if node.left:
        left = helper(node.left)
    if node.right:
        right = helper(node.right)
    
    if left:
        node.left = None
    if right:
        node.right = None
    return left and right and root.val == 0
