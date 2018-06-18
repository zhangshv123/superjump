#!/usr/bin/python
from collections import defaultdict
from collections import deque
class Solution(object):
	def verticalOrder(self, root):
#		这里把defaultdict的value设定为list类型
		vertical_map = defaultdict(list)
		if root is not None:
			self.bfs(root,vertical_map)
		res_list = []
		for key, value in sorted(vertical_map.items()): #注意vertical_map.items()返回一个tuple(A,B),然后按照A来排序
			res_list.append(value)
		return res_list
	
	def bfs(self,root,vetical_map):
		queue = deque()
		queue.append((0,root))
		while len(queue)>0:
			cur = queue.popleft()
			index,node = cur[0],cur[1]
			vetical_map[index].append(node.val)
			if node.left:
				queue.append((index-1,node.left))
			if node.right:
				queue.append((index+1,node.right))
