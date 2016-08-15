"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """
    Example:
        BT:
                        5
                3               7
            1       4       6       9
        Preorder:
            [5, 3, 1, 4, 7, 6, 9]
        Inorder:
            [1, 3, 4, 5, 6, 7, 9]

    Idea:
        - build the tree recursively by finding the root first.
        - root = first element of the preorder (sub) list.
        - then use inorder to separate left subtree sublist and right subtree sublist
        - then recursive call
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder is None or inorder is None:
            return None

        return self.buildTree_recursive(preorder, inorder, 0, len(preorder), 0, len(inorder))

    def buildTree_recursive(self, preorder, inorder, pre_start, pre_end, in_start, in_end):
        # base case
        if pre_start >= pre_end:
            return None

        root = TreeNode(preorder[pre_start])
        pos = in_start
        while pos < in_end:
            if preorder[pre_start] == inorder[pos]:
                break
            pos += 1

        root.left = self.buildTree_recursive(
                        preorder,
                        inorder,
                        pre_start + 1,
                        pre_start + pos - in_start + 1,  # exclusive
                        in_start,
                        pos
                    )
        root.right = self.buildTree_recursive(
                        preorder,
                        inorder,
                        pre_start + pos - in_start + 1,
                        pre_end,
                        pos + 1,
                        in_end
                    )

        return root
