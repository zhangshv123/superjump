写程序前先写好数学公式，搞清楚DFS的定义！
local = max(left+1(如果连上), right+1(如果连上),1)
global = max(local, globalLeft, globalRight)

class Solution(object):
	def longestConsecutive(self, root):
		res = self.dfs(root)
		return res[1]
	
	
	def dfs(self, root):
		if not root:
			return 0,0
		
		if not root.left and not root.right:
			return 1,1
		
#		left代表包含left node 的longestConsecutive 长度(local 变量)，gLeft代表root左边的全局longestConsecutive(全局变量)
		left, gLeft  = self.dfs(root.left)
		right, gRight = self.dfs(root.right)
		
#		local,global是整个题目的变量
		local = 1
		
		if root.left and root.val + 1 == root.left.val:
			local = max(local, left + 1)
					
		if root.right and root.val + 1 == root.right.val:
			local = max(local, right + 1)
			
		return local, max(local, gLeft, gRight)