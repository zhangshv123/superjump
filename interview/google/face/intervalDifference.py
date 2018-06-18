# 一道题给两个人的interval list. （interval由开始和结束组成， 每个人自己的interval可能有重合）找a的interval里不和b的interval重叠的部分。
"""
http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=359813&extra=page%3D1%26filter%3Dauthor%26orderby%3Ddateline%26sortid%3D311%26sortid%3D311%26orderby%3Ddateline
用线扫描 保存两个人在每个端点的interval数量即可 （代码默认 interval 左边inclusive, 右边exclusive）
"""
from collections import defaultdict
def getDifferenceInL(a, b):
    mp = defaultdict(lambda: defaultdict(int))
    a.sort(key = lambda k: k[0])
    b.sort(key = lambda k: k[0])
    for s, e in a:
        mp[s]['a'] += 1
        mp[e]['a'] -= 1
    for s, e in b:
        mp[s]['b'] += 1
        mp[e]['b'] -= 1
    start = -1
    cur = defaultdict(int)
    res = []
    for i in sorted(mp.keys()):
        cur['a'] += mp[i]['a']
        cur['b'] += mp[i]['b']
        if cur['a'] > 0 and cur['b'] == 0 and start == - 1:
            start = i
        if (cur['a'] == 0 or cur['b'] > 0) and start != - 1:
            res.append((start, i))
            start = -1
    return res
l = [[1, 2], [5, 7], [9, 10], [11, 12], [13, 14]]
r = [[2,6], [8, 17]]    
print(getDifferenceInL(l, r))