"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        cur = head
        m = {}
        while cur != None:
            m[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = head
        while cur != None:
            m[cur].next = m[cur.next] if cur.next != None else None
            m[cur].random = m[cur.random] if cur.random != None else None
            cur = cur.next
        return m[head] if head != None else None