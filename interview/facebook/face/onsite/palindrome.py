# 给定输入字符串，输出最长回文串，可通过删除字符或shuffle字符的操作
from collections import defaultdict
s = "adfadsfweewffdas"
m = defaultdict(int)
for c in s:
	m[c] += 1
half, single = [], '#'
for k, v in m.items():
	half += [k] * (v / 2)
	if v % 2 == 1:
		single = k
print "".join(half) + single + "".join(reversed(half))