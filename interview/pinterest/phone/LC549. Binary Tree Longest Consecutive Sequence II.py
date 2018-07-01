dfs:  以root为根节点向子节点方向（parent-child）的路径中，最大连续递增路径长度incal，以及最大连续递减路径长度decal
incal:包括root的最大连续递增路径长度
decal:包括root的最大连续递减路径长度
cincal:包含child的最大连续递增路径长度
这些都是local的变量
	
class Solution(object):
	glo = 0
	def longestConsecutive(self, root):
		if root:
			res = self.dfs(root)
		return self.glo
		
	def dfs(self, root): # root never being none
		incal,decal = 1, 1 # including self

		for child in (root.left, root.right):
			if child:            
				cincal, cdecal = self.dfs(child)
				if root.val + 1 == child.val:
					incal = max(cincal+1, incal)
				elif root.val - 1 == child.val:
					decal = max(cdecal+1, decal)

		self.glo = max(self.glo, incal + decal - 1)
		return incal, decal
		 
		
		
