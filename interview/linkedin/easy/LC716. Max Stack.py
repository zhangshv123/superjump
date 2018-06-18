class MaxStack(object):

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stk = []
		self.maxStack = []
		
	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		self.stk.append(x)
		if len(self.maxStack) == 0 or x >= self.maxStack[-1]:
			self.maxStack.append(x)

	def pop(self):
		"""
		:rtype: int
		"""
		if self.maxStack[-1] == self.stk.pop():
			self.maxStack.pop()
		

	def top(self):
		"""
		:rtype: int
		"""
		return self.stk[-1]
		

	def peekMax(self):
		"""
		:rtype: int
		"""
		return self.maxStack[-1]
		

	def popMax(self):
		"""
		:rtype: int
		"""
		# n=self.maxstk.pop()
		# i=len(self.stk)-1
		# tmp=[]
		# while n!=self.stk[-1]:
		#     tmp.append(self.pop())
		# ret=self.stk.pop()
		# for i in xrange(len(tmp)-1,-1,-1):
		#     self.push(tmp[i])
		# return ret
		
		res = None
		if len(self.maxStack) > 0:
			res = self.maxStack.pop()
			tmp = []
			item = self.stk.pop()
			while item:
				if item != res:
					tmp.append(item)
					item = self.stk.pop()

			while len(tmp) > 0:
				self.stk.append(tmp.pop())
		return res
			
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()