#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #heapq store [value, index, list]
        h = []
        dummy = ListNode(0)
        curNode = dummy
        for n in lists:
            if n != None:
                heapq.heappush(h, (n.val, n))
        while len(h) > 0:
            cur = heapq.heappop(h)
            node = cur[1]
            curNode.next = node
            curNode = curNode.next
            if node.next != None:
                heapq.heappush(h, (node.next.val, node.next))
        return dummy.next
            