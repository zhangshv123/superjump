"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        cur, preT = start, start
        while n >= 0:
            cur = cur.next
            n -= 1
        while cur != None:
            cur = cur.next
            preT = preT.next
        # print preT.val
        preT.next = preT.next.next
        return start.next