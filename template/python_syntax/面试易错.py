1.
return res.append(X)
错误！这里会返回 void!!!

2.
reverse 一个string
return str[::-1]

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
class pin(object):
	def __init__(self, id = 0, height = 0):
		self.id = id
		self.height = height

s = pin()
pin1 = pin(1,100)
pin2 = pin(2,200)
pin3 = pin(3,150)


7. set的方法：
https://www.programiz.com/python-programming/methods/set/remove
set只用add和remove，不要用什么POP!

8.defauldict
参见
http://tinyurl.com/ybprpfko
When each key is encountered for the first time, it is not already in the mapping; so an entry is automatically created using the default_factory function which returns an empty list. The list.append() operation then attaches the value to the new list. When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the list.append() operation adds another value to the list. 

9.初始化2维DP
dp = [[0 for _ in range(col)] for _ in range(row)] 
一定不能用其他方法初始化！

10.print是自动换行的，如果想不换行就加逗号
print "a",
print "b"
结果： a b

11.throw exception in python:
raise Exception('I know Python!') # Don't! If you catch, likely to hide bugs.

12. .sort和sorted的区别：
sorted() returns a new sorted list, leaving the original list unaffected. 
list.sort() sorts the list in-place, mutating the list indices, and returns None (like all in-place operations).
