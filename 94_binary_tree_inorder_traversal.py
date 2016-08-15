"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """
    Idea: 3 ways of doing it
        (1) Recursive (trivial) -> O(n) space
        (2) Iterative with Stack -> O(n) space
        (3) Morris Traversal -> O(1) space:
            - use 'curr' as current node, 'pre' for predecessor of 'curr'
            - check if left subtree exists
                * yes:
                    = find right most node in left tree
                    = check if it connects to 'curr'
                        * yes:
                            break it, visit 'curr', and move to right subtree
                        * no:
                            connect it, traverse left subtree
                * no:
                    = visit 'curr' node, then traverse right sub stree
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        pre = None
        curr = root

        while curr is not None:
            if curr.left is not None:
                pre = curr.left
                while pre.right is not None and pre.right != curr:
                    pre = pre.right
                if pre.right == curr:
                    pre.right = None
                    ret.append(curr.val)
                    curr = curr.right
                else:
                    pre.right = curr
                    curr = curr.left
            else:
                ret.append(curr.val)
                curr = curr.right

        return ret

    def inorderTraversal_stack(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        curr = root
        while len(stack) > 0 or curr is not None:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                # visit
                ret.append(curr.val)
                curr = curr.right

        return ret

    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root is None:
            return ret

        self.inorderTraversal_recursive_helper(root, ret)
        return ret

    def inorderTraversal_recursive_helper(self, node, ret):
        if node.left is not None:
            self.inorderTraversal_recursive(node.left, ret)

        ret.append(node.val)

        if node.right is not None:
            self.inorderTraversal_recursive(node.right, ret)
