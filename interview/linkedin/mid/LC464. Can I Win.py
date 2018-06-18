class Solution(object):
	def canIWin(self, maxChoosableInteger, desiredTotal):
		if (maxChoosableInteger+1) * maxChoosableInteger / 2 < desiredTotal: #数学公式（首项+末项）*项数/2
			return False
		if (maxChoosableInteger >= desiredTotal):
			return True
		used = 0
		mem = dict() # e.g., history["123"] = False, "123" == "321" == "231"
		# e.g., use 0000...01110 represents "123" used
		return self.helper(maxChoosableInteger, desiredTotal, used, mem)
					
	# dfs search + memorization
	def helper(self, maxChoosableInteger, desiredTotal, used, mem):
		if used in mem:
			return mem[used]
		for i in range(1, maxChoosableInteger+1):
			if not (1 << i & used): #0是FALSE，大于0是TRUE
				if desiredTotal <= i:
					mem[used] = True
					return True
				else:
					if not self.helper(maxChoosableInteger, desiredTotal - i, used | 1 << i, mem): # 00..01 << i(这里代表对手在这种情况下肯定赢不了，所以我肯定就赢了）
						mem[used] = True
						return True
		mem[used] = False
		return False

s = Solution()
print s.canIWin(10,11)
					
				
				
