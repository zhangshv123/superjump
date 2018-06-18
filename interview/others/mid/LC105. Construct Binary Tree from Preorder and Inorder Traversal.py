"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

前序遍历 1245367
中序遍历 4251637
后续遍历 4526731
具体到上面这一题，我们知道了一个二叉树的中序遍历以及后序遍历的结果，那么如何构建这颗二叉树呢？

仍然以上面那棵二叉树为例，我们可以发现，对于后序遍历来说，最后一个元素一定是根节点，也就是1。然后我们在中序遍历的结果里面找到1所在的位置，那么它的左半部分就是其左子树，有半部分就是其右子树。

我们将中序遍历左半部分425取出，同时发现后序遍历的结果也在相应的位置上面，只是顺序稍微不一样，也就是452。我们可以发现，后序遍历中的2就是该子树的根节点。

上面说到了左子树，对于右子树，我们取出637，同时发现后序遍历中对应的数据偏移了一格，并且顺序也不一样，为673。而3就是这颗右子树的根节点。

重复上述过程，通过后续遍历找到根节点，然后在中序遍历数据中根据根节点拆分成两个部分，同时将对应的后序遍历的数据也拆分成两个部分，重复递归，就可以得到整个二叉树了。
"""



"""
通过前序遍历和中序遍历的结果构造二叉树，我们只需要知道前序遍历的第一个值就是根节点，那么仍然可以采用上面提到的方式处理：

通过前序遍历找到根节点
通过根节点将中序遍历数据拆分成两部分
对于各个部分重复上述操作
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
	        ind = inorder.index(preorder.pop(0))
	        root = TreeNode(inorder[ind])
	        root.left = self.buildTree(preorder, inorder[0:ind])
	        root.right = self.buildTree(preorder, inorder[ind+1:])
	        return root