思路:
跟minstack那道题非常像，唯一不同的就只有popmax()函数
使用两个栈来模拟，s1为普通的栈，用来保存所有的数字，而s2为最大栈，用来保存出现的最大的数字。

在push()函数中，只有当maxstack为空，或者x>=maxstack才会放x进去maxtack

在pop()函数中，当s2的栈顶元素和s1的栈顶元素相同时，我们要移除s2的栈顶元素，因为一个数字不在s1中了，就不能在s2中。然后取出s1的栈顶元素，并移除s1，返回即可。

在top()函数中，直接返回s1的top()函数即可。

在peekMax()函数中，直接返回s2的top()函数即可。

在popMax()函数中，先将s2的栈顶元素保存到一个变量mx中，然后我们要在s1中删除这个元素，由于栈无法直接定位元素，所以我们用一个临时栈t，将s1的出栈元素保存到临时栈t中，当s1的栈顶元素和s2的栈顶元素相同时退出while循环，此时我们在s1中找到了s2的栈顶元素，分别将s1和s2的栈顶元素移除，然后要做的是将临时栈t中的元素加回s1中，注意此时容易犯的一个错误是，没有同时更新s2，所以我们直接调用push()函数即可
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
		:rtype: void
		"""
		cur = self.stk.pop()
		if self.maxStack[-1] == cur:
			self.maxStack.pop()
		return cur
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
		temp = []
		cur = self.maxStack.pop()
		while self.top() != cur:
			temp.append(self.stk.pop())
		self.stk.pop()
		while len(temp) > 0:
			self.push(temp.pop())
		return cur

obj = MaxStack()
obj.push(1)
obj.push(5); 
obj.push(1);
obj.push(5);
print obj.top()
print obj.popMax()
print obj.top()
print obj.peekMax()
print obj.pop()
print obj.top()	

#obj.push(5)
#obj.push(1)	
#print obj.popMax()	
#print obj.peekMax()

#obj.push(5)
#obj.push(1)	
#obj.push(-5)
#print obj.popMax()	
#print obj.popMax()
#print obj.top()
linkedin follow up:
implement 一个getMaxSum的方法，return stack里面所有正数的和 at any given time:
维护一个全局变量，push的时候，如果是正数，就加进去，负数就是0


