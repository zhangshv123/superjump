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