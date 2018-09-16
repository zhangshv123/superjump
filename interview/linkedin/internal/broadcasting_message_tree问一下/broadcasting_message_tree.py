思路：
如果是叶子节点，返回0
如果不是叶子节点，就把children的时间降序排列，然后选max的+i+1
时间复杂度：O(nlogn)
空间：O(n)
class TreeNode(object):
	def __init__(self, id, arr):
		self.id = id
		self.children = arr
		self.transmissionTime = 0

class Solution(object):
	def computeTransmissionTime(self, root):
		if not root or not root.children:
			return 0
		children = root.children
		for child in children:
			self.computeTransmissionTime(child)
		children.sort(key = lambda x: x.transmissionTime, reverse = True)
		minTransmissionTime = 0
		for i in range(len(children)):
			minTransmissionTime = max(minTransmissionTime, children[i].transmissionTime + i + 1)
		root.transmissionTime = minTransmissionTime
		return
	def mainMethod(self, root):
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
     /  \
    B     C
   / \   /
  D   E  F

输出
time(in second) transfer
1                 A->B
2                 A->B, C->F
3                 B->D
4                 B->E

	
		
		
		
		
