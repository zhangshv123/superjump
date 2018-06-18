from sets import Set
from collections import deque
"""
通过从输入字符串中移除每一个括号，生成新的字符串加入队列。

如果从队列中取出的字符串是有效的，则加入结果列表。

一旦发现有效的字符串，则不再向队列中补充新的可能字符串。

根据BFS的性质，当首次从队列中发现有效字符串时，其去掉的括号数一定是最小的。

而此时，队列中存在的元素与队头元素去掉的括号数的差值 ≤ 1

并且，只有与队头元素去掉括号数目相同的元素才有可能是候选答案（根据括号匹配的性质可知）
"""
class Solution(object):
	def removeInvalidParentheses(self, s):
		if self.isValid(s):
			return [s]
		q = deque()
		q.append(s)
		visited = set()
		visited.add(s)
		res = []
		while len(q) > 0:#BFS template
			size = len(q)
			for _ in range(size):
				cur = q.popleft()
				for i in range(len(cur)):
					del_cur = cur[:i] + cur[i+1:]
					if del_cur in visited:
						continue
					q.append(del_cur)
					visited.add(del_cur)
					if self.isValid(del_cur):
						res.append(del_cur)
			if len(res) > 0:#保证那一层至少有一个，然后就结束程序了！
				return res
		
		

	def isValid(self,s):
		stk = []
		for i in range(len(s)):
			if s[i] == '(':
				stk.append(s[i])
			elif s[i] == ')':
				if len(stk) == 0 or stk.pop() != '(':
					return False
		return len(stk) == 0
			