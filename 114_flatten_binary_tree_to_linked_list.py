"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree,
each node's right child points to the next node of a pre-order traversal.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """
    Idea:
        Recursive:
            - pre-order traversal of example tree:
                [3, 4, 2, 6, 5, 1]
            - recursive nature of the tree
        Iterative:
            - Add root's right sub-tree to left sub-tree's right most child
            - set root's right to left sub-tree
            - move root to root right
    """
    def flatten(self, root):
        while root is not None:
            if root.left is not None:
                n = root.left
                while n.right is not None:
                    n = n.right
                n.right = root.right
                # set root.right & root.left
                root.right = root.left
                root.left = None
            root = root.right

    def flatten_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        left = root.left
        right = root.right

        root.left = None
        self.flatten(left)
        root.right = left
        # link end of linked list to right sub-tree
        curr = root
        while curr.right is not None:
            curr = curr.right

        self.flatten(right)
        curr.right = right
