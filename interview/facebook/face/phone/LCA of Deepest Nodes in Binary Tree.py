给一个 二叉树 ， 求最深节点的最小公共父节点
		 1
	   2   3
		  5  6    return 3.

		 1  
	   2   3
   4      5 6   retrun 1. 
思路：
Recursion: 返回的时候返回lca和depth
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def deepestLowestCommonAncestor(self, root):
		return self.dfs(root)[1]
	
	def dfs(self, node):
		if not node:
			return (0, None)
				
		ldepth, lca = self.dfs(node.left)
		rdepth, rca = self.dfs(node.right)
		
		if ldepth == rdepth:
			return (ldepth+1, node.val)
		if ldepth > rdepth:
			return (ldepth+1, node.left.val)
		return (rdepth+1, node.right.val)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

s = Solution()
print s.deepestLowestCommonAncestor(root)

# BFS版本：
BFS层序遍历 找到全部最深子节点 ，同时维持一个父子关系的hash（最深子个数为1的时候直接输出爸爸）
其他情况一层一层往上找爸爸，当所有的爸爸都一样的时候输出就可以了。
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
from collections import deque, defaultdict
class Solution(object):
	def lowestCommonAncestor(self, root):
		q = deque()
		q.append(root)
		d = defaultdict(int)
		while len(q) > 0:
			size = len(q)
			deepest = []
			for i in range(size):
				cur = q.popleft()
				deepest.append(cur.val)
				if cur.left:
					q.append(cur.left)
					d[cur.left.val] = cur.val
				if cur.right:
					q.append(cur.right)
					d[cur.right.val] = cur.val
		if len(deepest) == 1:
			return d[deepest[0]]
		else:
			parent = set()
			for node in deepest:
				parent.add(d[node])
				deepest.remove(node)
			while len(parent) > 1:
				deepest = list(parent)
				for node in deepest:
					parent.remove(node)
					parent.add(d[node])
		return parent.pop()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
#root.right.right = TreeNode(7)

s = Solution()
print s.lowestCommonAncestor(root) 			