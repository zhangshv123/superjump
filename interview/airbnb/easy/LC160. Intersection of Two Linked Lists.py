"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getLen(node):
            l = 0
            while node != None:
                node = node.next
                l += 1
            return l
        la, lb = getLen(headA), getLen(headB)
        if la < lb:
            headA, headB = headB, headA
        for i in range(abs(la - lb)):
            headA = headA.next
        for i in range(min(la, lb)):
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
        return None
        
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getLength(head):
            l = 0
            while head != None:
                head = head.next
                l += 1
            return l
        la, lb = getLength(headA), getLength(headB)
        while la != lb:
            if la > lb:
                headA = headA.next
                la -= 1
            else:
                headB = headB.next
                lb -= 1
        while la > 0:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            la -= 1
        return None
            
            