# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temNode = stack.pop()
                ret.append(temNode.val)
                root = temNode.right
        return ret