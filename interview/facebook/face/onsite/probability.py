#!/usr/bin/python
"""
两种汤，各5000毫升，一个人有四种取法：100，0 / 50，50 / 75，25/ 25，75，每种取法概率一样0.25，问最后a种汤先被取完的概率
4种取法：
A汤取100，B汤取0
A汤取50，B汤取50
A取75，B取25
A取25，B取75. Waral 鍗氬鏈夋洿澶氭枃绔�,

"""
def prob():
	choices = [(100, 0), (50, 50), (75, 25), (25, 75)]
	m = {}
	def dfs(a, b):
		if (a, b) in m:
			return m[a, b]
		if a < 0:
			return (1, 0)
		elif b < 0:
			return (0, 1)
		else:
			countA, countB = 0, 0
			for da, db in choices:
				res = dfs(a - da, b - db)
				countA += res[0]
				countB += res[1]
			m[a, b] = (countA, countB)
			return (countA, countB)
	countA, countB = dfs(5000, 5000)
	return countA / (countA + countB)
print(prob())