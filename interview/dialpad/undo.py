题目：
operation             result
insert(0, abc)        abc
insert(3, xyz)        abcxyz
delete(2, 2)          abyz
undo()                abcxyz
undo()                abc
redo()                abcxyz
redo()                abyz

实现四个function
insert(index, string to insert)
delete(index, number of characters to remove)
redo()
undo()
思路：

有2个stk,一个undo, 一个redo
对于insert,delete，每次把结果放入undo
对于undo,把undo最后一个pop出来，放到redo里面，然后返回undo剩下的最后一个
对于redo，直接把redo的最后一个pop出来就好

redo的作用就是撤销undo的操作，undo是撤销上一个操作
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