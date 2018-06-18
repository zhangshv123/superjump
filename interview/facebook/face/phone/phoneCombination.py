#!/usr/bin/python
"""
这个时候就剩15分钟了，又来了一道题。是替换字母，特别简单，就递归一下就可以了. 
给一个Map<String, List<String>> sub. 其中key是要被替换的字母，list可以替换的一堆字母，输出所有可能 
E.G. 'a' -> {'b', 'c', 'd'}
那么一个word例如是abc，所有a都要被替换，那么输出就是{’abc','bbc','dbc'}
但是！！主要不是写程序！写程序就写了5分钟吧，分析复杂度分析了15分钟，有点蒙，讨论了好久也不知道自己说的复杂度对不对，感觉他对我的回答不是那么满意。。
"""
d = {
 '2':['a','b','c'],
 '3':['d','e','f'],
 '4':['g','h','i'],
 '5':['j','k','l'],
 '6':['m','n','o'],
 '7':['p','q','r','s'],
 '8':['t','u','v'],
 '9':['w','x','y','z']
    }
word = "2a3"
class Solution(object):
	def getAll(self, word):
		res = []
		def walk(w, idx):
			if idx == len(word):
				res.append(w)
			else:
				if word[idx] in d:
					for c in d[word[idx]]:
						walk(w + c, idx + 1)
				else:
					walk(w + word[idx], idx + 1)
		walk("", 0)
		return res
s = Solution()		
print s.getAll(word)