"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root
#BFS
from collections import deque
class Solution(object):
  def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
      return root
    q = deque()
    q.append(root)
    while len(q) > 0:
      cur = q.popleft()
      left = cur.left
      cur.left = cur.right
      cur.right = left
      
      if cur.left:
        q.append(cur.left)
      if cur.right:
        q.append(cur.right)
    return root