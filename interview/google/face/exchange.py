# 给两个string a, b，它们的距离定义为对应位置字符不同的个数。现在可以把a任意两个位置的字符交换一次， 问怎么交换使得距离最小。
from collections import defaultdict
def exchange(a, b):
    m = defaultdict(set)
    for i, (ca, cb) in enumerate(zip(a, b)):
        if ca != cb:
            m[ca].add((cb, i))
    print m         
    res = (-1, -1)
    for ca, s in m.items():
        for cb, i in s:
            if cb in m:
                for ck, k in m[cb]:
                    if ck == ca:
                        return (i, k)
                    res = (i, k)
    return res            
print(exchange("afffdaa", "agdgfaa"))