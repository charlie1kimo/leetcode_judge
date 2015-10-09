"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        return max(
            self.findMaxDepth(root.left, 1),
            self.findMaxDepth(root.right, 1)
        )

    def findMaxDepth(self, node, depth):
        if node == None:
            return depth

        return max(
            self.findMaxDepth(node.left, depth+1),
            self.findMaxDepth(node.right, depth+1)
        )
