"""
 就是一个binary search tree， 给你个 target ， 一个k, 然后让你找出距离这个target距离最近的K个element。（距离的定义就是binary tree里面value的值 到这个target的绝对值）
"""
import heapq
class Solution(object):
    def getcloseK(r, k):
        h = []
        def walk(r):
            if r != None:
                dis = abs(r.val - target)
                if len(h) < k:
                    #maxHeap
                    heapq.heappush(h, (-dis, r.val))
                else:
                    if -h[0][0] > dis:
                        heapq.heapreplace(h, (-dis, r.val))
                walk(r.left)
                walk(r.right)