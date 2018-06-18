"""
国人大叔，两个string 都有字母或者backspace，然后看最后是不是一样的结果，觉得应该有原题，奈何没刷，不过先brutal用了两个stack，后来说指针，大叔直接跟我说你别从头到尾，你从尾到头嘛。。
"""

#!/usr/bin/python
def check(s, t, b):
	def getInd(i, ss):
		# if b, move 2 
		while i >= 0 and ss[i] == b:
			i -= 2
		return i
	i, j = len(s) - 1, len(t) - 1
	while i >= 0 and j >= 0:
		i, j = getInd(i, s), getInd(j, t)
		if s[i] == -1 or t[j] == -1 or s[i] != t[j]:
			return False
		i -= 1
		j -= 1
	return True

s, t = "sts-a", "stt-"
b = "-"	
print check(s, t, b)