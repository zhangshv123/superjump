#题目：
#一个binary search tree 
#给两个点
#找到这两个点之间的path
#有可能点不在tree中 则throw一个exception.
思路：
先用findpath分别找到这2个点的路径，得到pathp, pathq,然后再类似最近公共祖先那样把2个path merge一下
from collections import defaultdict
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def findPathForNodesInBST(self, root, p, q):
		pathp = self.findPath(root, p)
		pathq = self.findPath(root, q)
		res = []
		if len(pathp) == 0 or len(pathq) == 0:
			raise Exception
		d = defaultdict(int)
		startp = -1
		startq = -1
		print pathp, pathq
		for i,val in enumerate(pathp):
			d[val] = i
		pathq.reverse()
		for i,val in enumerate(pathq):
			if val in d:
				startp = d[val]
				startq = i
		return pathq[:startq] + pathp[startp:]
	
	def findPath(self, root, node):
		path = []
		while root:
			path.append(root.val)
			if node.val > root.val:
				root = root.right
			elif node.val < root.val:
				root = root.left
			else:
				return path
		return path

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(1)
root.right.right = TreeNode(5)

s = Solution()
print s.findPathForNodesInBST(root, root.left.left, root.right.right)
		