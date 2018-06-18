"""
example tree:
     1 
   / | \
  2  3  4
/|\    |
5 8 6   7
   / \
  9   10

上来贴了一个树和一个node结构，说要完成这么个function。我没懂什么顺序，prev_node到底指啥，就问了一下，最后讨论出来可以按照pre-order顺序看， Order: 1, 2, 5, 8, 6, 9, 10, 3, 4, 7
在这里，input不是root，而是target，可以是tree里任何一个node,找它的prev_node。
input：2  output: 1
input: 3  output: 10
input: 4  output: 3
"""
class Node:
    def __init__(self):
        self.parent = None
        self.first_sibling = None
        self.next_sibling = None
        self.first_child = None
        self.last_child
        
def getPreNode(node):
    if node == node.first_sibling:
        return node.parent
    pre, cur = node.first_sibling, node.first_sibling
    while cur != None:
        pre =  cur
        cur = next_sibling
        if cur == node:
            while pre.first_child != None:
                pre = pre.last_child
            return pre
    return None
                