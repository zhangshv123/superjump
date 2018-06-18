#!/usr/bin/python
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        nextNode = head.next
        head.next = None
        newHead = self.reverse(nextNode)
        nextNode.next = head
        return newHead
        
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        dummyNode = ListNode(0)
        tail = dummyNode
        while True:
            nH = cur
            for _ in range(k - 1):
                if cur is None:
                    break
                cur = cur.next
            if cur is None:
                tail.next = nH
                break
            nextGroupHead = cur.next
            cur.next = None
            tail.next = self.reverse(nH)
            tail = nH
            cur = nextGroupHead
        return dummyNode.next