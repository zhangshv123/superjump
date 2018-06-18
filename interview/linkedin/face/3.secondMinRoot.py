#好像在面经里看到过，bianry tree, 每个节点下有0或2个子节点，每个节点的值都是两个子节点的最小值，让你找second min。
#     2.
#   /    \
#  2      5
#/  \    / \
#2  4   5   6
import heapq
class Solution(object):
    def getSecondMin(r):
        h = []
        def walk(r):
            if None not in [r, r.left, r.right]:
                if r.left.val == r.val:
                    heapq.heappush(h, r.right.val)
                    walk(r.left)
                else:
                    heapq.heappush(h, r.left.val)
                    walk(r.right)
        return h[0]