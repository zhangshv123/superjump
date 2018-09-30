思路：
先把tree变成一个graph，然后用拓扑排序来做！建graph的过程跟LC742有点像
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
from collections import defaultdict, deque
class Solution(object):
	def findLeaves(self, root):
		res = []
		if not root:
			return res
		if not root.left and not root.right:
			return [[root.val]]
		
		out_d = defaultdict(TreeNode)
		in_d = defaultdict(int)
		q = deque()
		self.buildGraph(root, None, out_d, in_d)
		for key in in_d.keys():
			if in_d[key] == 0:
				q.append(key)
					
		while len(q) > 0:
			size = len(q)
			layer = []
			for i in range(size):
				cur = q.popleft()
				layer.append(cur.val)
				if cur in out_d:
					parent = out_d[cur]
					in_d[parent] -= 1
					if in_d[parent] == 0:
						q.append(parent)
			res.append(layer)
		return res
				
	def buildGraph(self, node, parent, out_d, in_d):
		if not node:
			return
		if parent:
			out_d[node] = parent
			in_d[parent] += 1
			in_d[node] = 0
			
		self.buildGraph(node.left, node, out_d, in_d)
		self.buildGraph(node.right, node, out_d, in_d)
		return
				
root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)

s = Solution()
print s.findLeaves(root)