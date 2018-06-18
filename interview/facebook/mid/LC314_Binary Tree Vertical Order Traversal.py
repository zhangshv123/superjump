"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""
# 方法：以列为键值，将节点保存在哈希映射的列表中。广度优先搜索。
from collections import deque
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = deque()
        if root != None:
            q.append((0, root))
        index_map = defaultdict(list)
        while len(q) > 0:
            cur = q.popleft()
            index,node = cur
            index_map[index].append(node.val)
            if node.left != None:
                q.append((index - 1, node.left))
            if node.right != None:
                q.append((index + 1, node.right))
        return map(lambda item: item[1], sorted(index_map.items()))
            