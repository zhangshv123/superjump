#!/usr/bin/python
#题目是：如果我们有random5(得到一个数0-4的随机数)，implement一个random7
#这个网址讲得不错：http://www.growingwiththeweb.com/2014/03/given-random5-implement-random7.html
import random
def random5():
	return random.randint(0, 4)

def random7():
	current = 5*random5()
	if current > 20:
		return random7()
	else:
		return current%7

print random5()
print random7()