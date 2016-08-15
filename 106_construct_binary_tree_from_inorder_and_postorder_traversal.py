"""
Given inorder and postorder traversal of a tree, construct the binary tree.

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
        Postorder:
            [1, 4, 3, 6, 9, 7, 5]
    Idea:
        - build the tree recursively by finding the root first.
        - root = last element of the postorder (sub) list.
        - then use inorder to separate left subtree sublist and right subtree sublist
        - then recursive call
    """
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None or postorder is None:
            return None

        return self.buildTree_recursive(inorder, postorder, 0, len(inorder), 0, len(postorder))

    def buildTree_recursive(self, inorder, postorder, in_start, in_end, post_start, post_end):
        # base case
        if in_start >= in_end:
            return None

        root = TreeNode(postorder[post_end - 1])
        pos = in_start
        while pos < in_end:
            if inorder[pos] == postorder[post_end - 1]:
                break
            pos += 1

        root.left = self.buildTree_recursive(
            inorder,
            postorder,
            in_start,
            pos,  # exclusive
            post_start,
            post_start + pos - in_start  # exclusive
        )
        root.right = self.buildTree_recursive(
            inorder,
            postorder,
            pos + 1,
            in_end,
            post_end - (in_end - pos),
            post_end - 1
        )

        return root
