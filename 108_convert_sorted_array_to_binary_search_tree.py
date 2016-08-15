"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
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
        - grab mid, and then partition the list into left and right
        - recursively build the left tree and right tree
    """
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBST_recursive(nums)

    def sortedArrayToBST_recursive(self, nums):
        # base case
        if len(nums) == 0:
            return None

        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST_recursive(nums[:mid])
        root.right = self.sortedArrayToBST_recursive(nums[mid+1:])

        return root
