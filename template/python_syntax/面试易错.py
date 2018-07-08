1.
return res.append(X)
错误！这里会返回 void!!!

2.
print 2+"3"
TypeError: unsupported operand type(s) for +: 'int' and ‘str'

3.
result type
返回的东西不止一种信息怎么办？
用全局变量！
经典题目
https://www.jiuzhang.com/solutions/minimum-subtree/#tag-highlight-lang-python

4.
改变str的char,要用replace方法
str = "this is a"
str = str.replace("is", "was")
print str

5.全局变量！
1）写在class里面，def前面，这样里面用的时候都是self.glo
class Solution(object):
	glo = 0
	def longestConsecutive(self, root):
		if root:
			res = self.dfs(root)
		return self.glo
		
6.初始化object的方式
看resize_page.py
class pin:
	def __init__(self, id = 0, height = 0):
		self.id = id
		self.height = height

s = pin()
pin1 = pin(1,100)
pin2 = pin(2,200)
pin3 = pin(3,150)