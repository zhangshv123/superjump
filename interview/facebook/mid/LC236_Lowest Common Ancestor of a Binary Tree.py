#!/usr/bin/python
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

          _______3______
         /              \
     ___5__          ___1__
    /      \        /      \
    6      _2       0       8
            /  \
            7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Show Company Tags
Show Tags
Show Similar Problems

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://www.hrwhisper.me/algorithm-lowest-common-ancestor-of-a-binary-tree/
"""
思想：和数学归纳法一样， 提取树里的信息，得到答案
1.从子树传递上来的信息是什么？
2.自己要做什么？
hasLeft, hasRight
y           y
y           n
n           y
n           n
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q :
            return root
        left, right = None, None
        if root.left:
            left = self.lowestCommonAncestor(root.left,p,q)
        if root.right:
            right = self.lowestCommonAncestor(root.right,p,q)
        
        if left and right:
            return root
        elif right and not left:
            return right
        else:
            return left


鑫鑫的non-recursive版本：
stack存的分别是：[current node, is_left_done, is_right_done, leftNode, rightNode]
ret代表原来recursive 版本的返回值
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stk = []
        stk.append([root, False, False, None, None])
        while len(stk) > 0:
            curr = stk[-1]
            if curr[0]== p or curr[0] == q or not curr[0]:
                ret = curr[0]
                stk.pop()
                if len(stk)>0:
                    if not stk[-1][1]: #如果左边没有做完，is_left_done = False的话
                        stk[-1][1] = True
                    else: #说明左边做完了，那就是右边没有做完，is_right_done = False的话
                        stk[-1][2] = True                
                continue
            if not curr[1]: #如果左边没有做完,我们就左边，初始化都是false和None,代表新的节点(curr[0].left)左右节点都还没做过，返回的也都是None
                stk.append([curr[0].left, False, False, None, None])
            elif not curr[2]: #说明左边做完了，那就是右边,那左边返回letNode = ret
                curr[3] = ret
                stk.append([curr[0].right, False, False, None, None])
            else: #左右2边都做完了
                curr[4] = ret #先更新右边节点
                left, right = curr[3], curr[4]
                if left and right:
                    ret = curr[0]
                elif not left and right:
                    ret = right
                else:
                    ret = left
                stk.pop()
                if len(stk)>0:
                    if not stk[-1][1]:
                        stk[-1][1] = True #告诉parent节点，它的左右都已经做过了
                    else:
                        stk[-1][2] = True
        return ret


"""
分别找到p,q对应的path,遍历两个path找到最后一个相同的元素
"""
class Solution(object):
    def getPath(self, root, p):
        stk, path = [], []
        if root != None:
            stk.append((root, 0))
        while len(stk) > 0:
            node, height = stk.pop()
            if len(path) <= height:
                path.append(node)
            else:
                path[height] = node
            if node == p:
                return path[:height + 1]
            if node.left != None:
                stk.append((node.left, height + 1))
            if node.right != None:
                stk.append((node.right, height + 1))
        return []
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1, path2 = self.getPath(root, p), self.getPath(root, q)
        if len(path1) == 0 or len(path2) == 0:
            return None
        min_length = min(len(path1), len(path2))
        for i in range(1, min_length + 1):
            if i == min_length or path1[i] != path2[i]:
                return path1[i-1]
 
#niuniu version               
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        stk,path,res = [],[],[]
        if root != None:
            stk.append((root,0))
        while len(stk) > 0:
            node,height = stk.pop()
            if len(path) <= height:
                path.append(node.val)
            else:
                path[height] = node.val
            
            # base
            if node == p:
                res.append(path[:height+1])
            elif node == q:
                res.append(path[:height+1])
            if len(res) == 2:
                break
            if node.left:
                stk.append((node.left,height+1))
            if node.right:
                stk.append((node.right,height+1))
            
        i = 1
        min_length = min(len(res[0]),len(res[1]))
        for i in range(1, min_length + 1):
            if i == min_length or res[0][i] != res[1][i]:
                return res[0][i-1]

# 如果存在parent节点
class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """ 
    def lowestCommonAncestorII(self, root, A, B):
        # Write your code here
        dict = {}
        while A is not None:
            dict[A] = True
            A = A.parent

        while B is not None:
            if B in dict:
                return B
            B = B.parent

        return root

#如果2个节点可能一个存在，一个不存在tree里面，或者2个都不存在tree里面
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        a = [False]
        res = self.dfs(root, p, q, a)
        if a[0] is True:
            return res
        else:
            return None

    def dfs(self, root, p, q, a):
        """
        :rtype: TreeNode
        """
        if not root:
            return None
        left = self.dfs(root.left, p, q, a)
        right = self.dfs(root.right, p, q, a)
        if root == p or root == q:
            if left or right:
                # found the LCA
                a[0] = True
                return root
            else:
                return root
        if left and not right:
            return left
        if right and not left:
            return right
        if not left and not right:
            return None
        # found the LCA
        a[0] = True
        return root


        # Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stk = []
        stk.append([root, False, False, None, None])
        while len(stk) > 0:
            curr = stk[-1]
            print curr
            if curr[0]== p or curr[0] == q or not curr[0]:
                ret = curr[0]
                stk.pop()
                if len(stk)>0:
                    if not stk[-1][1]:
                        stk[-1][1] = True
                    else:
                        stk[-1][2] = True                
                continue
            if not curr[1]:
                stk.append([curr[0].left, False, False, None, None])
            elif not curr[2]:
                curr[3] = ret
                stk.append([curr[0].right, False, False, None, None])
            else:
                curr[4] = ret
                left, right = curr[3], curr[4]
                if left and right:
                    ret = curr[0]
                elif not left and right:
                    ret = right
                else:
                    ret = left
                stk.pop()
                if len(stk)>0:
                    print stk
                    if not stk[-1][1]:
                        stk[-1][1] = True
                    else:
                        stk[-1][2] = True
        return ret

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
#root.right.left = TreeNode(6)
#root.right.right = TreeNode(7)

s = Solution()
print s.lowestCommonAncestor(root, root.right, root.left.left)        
        
