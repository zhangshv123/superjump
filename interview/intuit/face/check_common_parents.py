"""
题意是：假设我们有一个graph，input data是parent child的形式，格式是一个(parent, child) pairs的list，每一个节点都有一个unique integer identifier
比如：
1   2   4
  \ /   / \ 
   3   5   8
    \ / \   \
     6   7   9
input就是int[][] parentChildPairs = new int[][] { {1, 3}, {2, 3}, {3, 6}, {5, 6}, {5, 7}, {4, 5}, {4, 8}, {8, 9}};
第一问：求两个list，一个list是没有任何parent的list，另一个是只有一个parent的list. 1point3acres.com/bbs
比如这个图的结果就是[[1, 2, 4], [5, 8, 7, 9]] （我是用List<List<Integer>>表示的）
第二问：给两个node接点，返回是否有公告祖先
parentChildPairs, 3, 8 => false
parentChildPairs, 5, 8 => true
parentChildPairs, 6, 8 => true
"""
from collections import defaultdict
def check(pairs, l):
	parents = defaultdict(set)
	for a, b in pairs:
		parents[b].add(a)
	res = []
	def findParents(n):
		if not parents[n]:
			return {n}
		s = set()
		for m in parents[n]:
			s |= findParents(m)
		return s
	for a, b in l:
		res += bool(findParents(a).intersection(findParents(b))),
	return res
pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9)]
l = [(3, 8), (5, 8), (6, 8)]
print check(pairs, l)