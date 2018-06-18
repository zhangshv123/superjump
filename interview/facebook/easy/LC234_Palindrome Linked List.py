#!/usr/bin/python
"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        stk = []
        while fast != None and fast.next != None:
            stk.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        while slow != None:
            if slow.val != stk.pop():
                return False
            slow = slow.next
        return True