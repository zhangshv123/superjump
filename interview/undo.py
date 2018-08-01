有2个stk,一个undo, 一个redo
对于insert,delete，每次把结果放入undo
对于undo,把undo结果pop出来，放到redo里面
对于redo，把直接把redo的最后一个pop出来就好
class Solution(object):
	result = ""
	undo = []
	redo = []
		
	def mainTest(self):
		print self.insert(0, "abc")
		print self.insert(3, "xyz")
		print self.delete(2, 2)
		print self.undoAction()
		print self.undoAction()
		print self.redoAction()
		print self.redoAction()
		
	
	def insert(self, start, str):
		global result
		if start >= len(self.result):
			self.result += str
		else:
			self.result = self.result[:start] + str + self.result[start]
		self.undo.append(self.result)
		return self.result
		
	def delete(self, start, num):
		global result
		if start >= len(self.result):
			return ""
		self.result = self.result[:start]+ self.result[start+num:]
		self.undo.append(self.result)
		return self.result
	
	def redoAction(self):
		global result
		self.result = self.redo.pop()
		return self.result
		
	def undoAction(self):
		self.redo.append(self.undo.pop())
		self.result = self.undo[-1]
		return self.result

s = Solution()
s.mainTest()	