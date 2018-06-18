"""
写一个random 输出城市名字的函数。给了一个城市的map，格式：城市名，人口数。根据城市人口数的比例，来输出城市名字。
比如 map：DC 90， SF 50， LA 60，城市输出的概率分别是：90/200， 50/200， 60/200. 不停的掉用这个函数,
按照概率来输出城市的名字
"""
import random
class weightChar(object):
	def __init__(self, cities):
		self.s = 0
		self.sums = []
		for city, num in cities.items():
			self.s += num
			self.sums.append((self.s, city))
	def getRandomCity(self):
		t = random.randrange(1, self.s)
		ss = self.sums
		l, r = 0, len(ss) - 1
		while l < r:
			m = l + (r - l) / 2
			if ss[m][0] <= t:
				l = m + 1
			else:
				r = m - 1
		return ss[l][1]
				
s = weightChar({"DC":90,"SF":50,"LA":60})
print s.getRandomCity()