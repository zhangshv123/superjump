# implement an iterator API with only next() function to get node from BT with preorder traversal. 
# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = [root]

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stk) != 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stk.pop()
        if node.right != None:
            self.stk.append(node.right)
        if node.left != None:
            self.stk.append(node.left)
        return node.val

# Your BSTIterator will be called like this:
a, b, c, d, e =  TreeNode(5), TreeNode(3), TreeNode(1), TreeNode(4), TreeNode(7) 
a.left, a. right = b, e
b.left, b.right = c, d   
i, v = BSTIterator(a), []
while i.hasNext(): 
    print("A")
    v.append(i.next())
print(v)    