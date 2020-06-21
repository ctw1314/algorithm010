class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ret, level = [], [root]
        while any(level):
            ret.append([node.val for node in level])
            level = [child for node in level for child in node.children if child]
        return ret