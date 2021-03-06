#!/usr/bin/python
#先中序遍历，然后用heap找到最接近的K个
时间复杂度： o(nlogn)
class Solution(object):
	def closestKValues(self, root, target, k):
		heap = []
		self.dfs(root, target, heap)
			  
		output = []
		for _ in range(k):
			output.append(heapq.heappop(heap)[1])
		return output
		
	def dfs(self, root, target, heap):
		if root is None:
			return

		self.dfs(root.left, target, heap)
		heapq.heappush(heap, (abs(root.val - target), root.val))
		self.dfs(root.right, target, heap)

# 还有一种解法是直接在中序遍历的过程中完成比较，当遍历到一个节点时，如果此时结果数组不到k个，
# 我们直接将此节点值加入res中，如果该节点值和目标值的差值的绝对值小于res的首元素和目标值差值的绝对值，
# 说明当前值更靠近目标值，则将首元素删除，末尾加上当前节点值，反之的话说明当前值比res中所有的值都更偏离目标值，
# 由于中序遍历的特性，之后的值会更加的遍历，所以此时直接返回最终结果即可
# http://tinyurl.com/yamoya2z
时间复杂度： o(n) 更快！
from collections import deque
class Solution(object):
	def closestKValues(self, root, target, k):
		res = deque()
		self.dfs(root, target, k, res)
		return list(res)
		
	def dfs(self, node, target, k, res):
		if not node:
			return
		
		self.dfs(node.left, target, k, res)
		if len(res) < k:
			res.append(node.val)
		elif abs(node.val - target) < abs(res[0] - target):
			res.popleft()
			res.append(node.val)
		else:
			return
		self.dfs(node.right, target, k, res)