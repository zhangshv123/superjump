class MaxStack(object):

			def __init__(self):
				"""
				initialize your data structure here.
				"""
				self.stack = []
				self.stack2 = []

			def push(self, x):
				"""
				:type x: int
				:rtype: void
				"""
				if len(self.stack) != 0:
					self.stack.append((x, max(x, self.peekMax())))
				else:
					self.stack.append((x, x))

			def pop(self):
				"""
				:rtype: int
				"""
				if len(self.stack) == 0:
					return None
				return self.stack.pop()[0]

			def top(self):
				"""
				:rtype: int
				"""
				if len(self.stack) == 0:
					return None
				return self.stack[-1][0]

			def peekMax(self):
				"""
				:rtype: int
				"""
				if len(self.stack) == 0:
					return None
				return self.stack[-1][1]

			def popMax(self):
				"""
				:rtype: int
				"""
				if len(self.stack) == 0:
					return None
				while self.peekMax() != self.top():
					self.stack2.append(self.pop())
				val = self.pop()
				while len(self.stack2) != 0:
					self.push(self.stack2.pop())
				return val