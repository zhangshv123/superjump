参考https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
	 a) Pop the top item from stack.
	 b) Print the popped item, set current = popped_item->right 
	 c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
class Solution(object):
	def inorderTraversal(self, root):
		res = []
		stk = []
		cur = root
		while cur or len(stk) > 0:
			while cur:
				stk.append(cur)
				cur = cur.left
			cur = stk.pop()
			res.append(cur.val)
			cur = cur.right
		return res
