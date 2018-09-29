思路：
如果是叶子节点，返回0
如果不是叶子节点，就把children的时间降序排列，然后选max的+i+1
n是number of nodes in tree
时间复杂度：O(nlogn)
空间：O(n)
from collections import defaultdict
class TreeNode(object):
	def __init__(self, id, arr):
		self.id = id
		self.children = arr
		self.transmissionTime = 0

class Solution(object):
	def computeTransmissionTime(self, root):
		if not root or not root.children:
			return
		children = root.children
		for child in children:
			self.computeTransmissionTime(child)
			
		children.sort(key = lambda x: x.transmissionTime, reverse = True)
		m = 0
		for i in range(len(children)):
			m = max(children[i].transmissionTime + i + 1, m)
		root.transmissionTime = m
		return
	def mainMethod(self, root):
		d = defaultdict(list)
		self.computeTransmissionTime(root)
		return root.transmissionTime

node6 = TreeNode(6, None)
node5 = TreeNode(5, None)
node4 = TreeNode(4, None)
node2 = TreeNode(2, [node4, node5, node6])
node3 = TreeNode(3, None)
node1 = TreeNode(1, [node2, node3])


s = Solution()
print s.mainMethod(node1)

linkedin follow up:
把每步的情况打印出来
比如：
       A
     /   \
    B     C
   / \   /
  D   E  F

输出
time(in second) transfer
1                 A->B
2                 A->B, C->F
3                 B->D
4                 B->E

思路：
D : 0秒, []
B : 2秒， [B->D, B->E]         +1
			dict[0] : B->D
			dict[1] : B->E
			
C : 1秒     dict[0] :  C->F    +2
A : 3秒     dict[0] : A->B
		    dict[1] : A->C   B->D
			dict[2] : B->E   C->F
		
from collections import defaultdict
class TreeNode(object):
	def __init__(self, id, arr):
		self.id = id
		self.children = arr
		self.transmissionTime = 0
		self.steps = []

class Solution(object):
	def computeTransmissionTime(self, root):
		if not root or not root.children:
			return
		children = root.children
		for child in children:
			self.computeTransmissionTime(child)
			
		children.sort(key = lambda x: x.transmissionTime, reverse = True)
		m = 0
		for i in range(len(children)):
			m = max(children[i].transmissionTime + i + 1, m)
		root.transmissionTime = m
		root.steps = [[] for i in range(m)]
		for i in range(len(children)):
			root.steps[i].extend(['{}->{}'.format(root.id, children[i].id)])
			for j in range(len(children[i].steps)):
				root.steps[i + j + 1].extend(children[i].steps[j])
		return
	def mainMethod(self, root):
		d = defaultdict(list)
		self.computeTransmissionTime(root)
		return root.steps, root.transmissionTime
node7 = TreeNode(7, None)
node8 = TreeNode(8, None)
node9 = TreeNode(9, None)
node6 = TreeNode(6, None)
node5 = TreeNode(5, None)
node4 = TreeNode(4, [node7, node8, node9])
node2 = TreeNode(2, [node4, node5, node6])
node3 = TreeNode(3, None)
node1 = TreeNode(1, [node2, node3])


s = Solution()
print s.mainMethod(node1)
	
		
		
		
		
