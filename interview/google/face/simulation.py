#!/usr/bin/python
"""
白人小哥，看起来就智商很高的那种。题目是给一瓶药，里面100颗完整的药片，每天需要吃半颗。每天吃的方法是随机从瓶子里
取一颗药，如果是整颗就吃半颗，剩下半颗扔回瓶子里；如果取出的是半颗，那就直接吃掉。第一小问是simulate这个过程，
然后print每天瓶中剩下的整颗和半颗的数量，直到空瓶。第二问是，求整个simulation过程中，瓶中剩下1整颗，0半颗的概率。
最后问了running time
"""
import random
class Simulation(object):
	def __init__(self, N):
		self.m = [2] * N
		self.f = N
		self.h = 0
	def take(self):
		idx = random.randrange(self.f + self.h)
		self.m[idx] -= 1
		if self.m[idx] == 1:
			self.f -= 1
			self.h += 1
		elif self.m[idx] == 0:
			self.m[idx] = self.m[self.f + self.h - 1]
			self.m[self.f + self.h - 1] = 0
			self.h -= 1
	def simulate(self, f, h):
		while self.f + self.h > 0:
			self.take()
			if self.f == f and self.h == h:
				return True
		return False
def test(N, f, h):
	M = 0				
	for i in range(N):
		s = Simulation(100)
		if s.simulate(f, h):
			M += 1
	return M / N
print(test(100, 1, 0))
		
		