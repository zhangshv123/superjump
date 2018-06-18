# 反转有环的链。 例如 A->B->C->D->A 转换成A<-B<-C<-D<-A
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def reverseList(node):
    prev, cur, next = node, node.next, node.next.next
    while cur != node:
        cur.next = prev
        prev, cur, next = cur, next, next.next
    cur.next = prev

def printList(node):
    head = node
    while node.next != head:
        print(node.val)
        node = node.next
    print(node.val)
a, b, c, d = ListNode("a"), ListNode("b"), ListNode("c"), ListNode("d")    
a.next, b.next, c.next, d.next = b, c, d, a
printList(a)
reverseList(a)
printList(a)