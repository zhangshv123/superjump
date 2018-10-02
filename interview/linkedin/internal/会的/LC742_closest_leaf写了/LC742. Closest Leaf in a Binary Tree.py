思路：这道题真不简单！先把tree的存储结构变成无向图的存储结构(只能是无向图，因为要做BFS)，然后从k开始BFS第一个找到的leaf节点一定是最短的！
具体请看花花视频
https://zxi.mytechroad.com/blog/tree/742-closest-leaf-in-a-binary-tree/
time: O(n)
space: O(n)
from collections import defaultdict,deque
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution(object):
	start = None
	def findClosestLeaf(self, root, k):
		if not root.left and not root.right and root.val == k:
			return k
		d = defaultdict(list)
		self.buildGraph(root, None, k, d)
		q = deque()
		q.append(self.start)
		level = 0
		visited = set()
		visited.add(self.start)
		while len(q) > 0:
			size = len(q)
			for i in range(size):
				cur = q.popleft()
				if not cur.left and not cur.right:
					return cur.val
				for child in d[cur]:
					if child not in visited:
						visited.add(child)
						q.append(child)
		return 0
						
	def buildGraph(self, node, parent, k, d):
		if not node:
			return
		if node.val == k:
			self.start = node
		if parent:
			d[parent].append(node)
			d[node].append(parent)
		self.buildGraph(node.left, node, k, d)
		self.buildGraph(node.right, node, k, d)
		return

root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)
#root.right.left = TreeNode(6)
#root.right.right = TreeNode(7)

s = Solution()
print s.findClosestLeaf(root, 1)   

linkedin follow up:
	find all K distance nodes  		
		