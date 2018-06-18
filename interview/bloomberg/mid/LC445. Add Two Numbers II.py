# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		stk1 = []
		stk2 = []
		while l1:
			stk1.append(l1.val)
			l1 = l1.next
			
		while l2:
			stk2.append(l2.val)
			l2 = l2.next
		
		lst = ListNode(0)
		total = 0
		while len(stk1) > 0 or len(stk2) > 0:
			if len(stk1) > 0:
				total += stk1.pop()
			if len(stk2) > 0:
				total += stk2.pop()
			lst.val = total%10
			total = total/10
			head = ListNode(total)
			head.next = lst
			lst = head
		
		return lst.next if lst.val == 0 else lst
			
			
			
		