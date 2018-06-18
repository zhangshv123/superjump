#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        second_node = head.next
        head.next = None
        new_head = self.reverseList(second_node)
        second_node.next = head
        return new_head