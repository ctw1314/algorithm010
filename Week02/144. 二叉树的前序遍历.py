Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def preorderTraversal(self, root):
        ret, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                #注意压入栈的顺序,先压入右孩子，再压入左孩子
                stack.append(node.right)
                stack.append(node.left)
        return ret     