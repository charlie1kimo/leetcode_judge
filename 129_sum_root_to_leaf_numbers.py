"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25. 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        return self.sumNumsHelper(0, [], root)

    def sumNumsHelper(self, total, path, node):
        path.append(node.val)
        
        # base case; lefat node
        if node.left == None and node.right == None:
            num_str = "".join(map(str, path))
            num = int(num_str)
            total += num
            return total

        left = 0
        right = 0
        if node.left != None:
            left = self.sumNumsHelper(total, list(path), node.left)
        if node.right != None:
            right = self.sumNumsHelper(total, list(path), node.right)
        
        return total + left + right
