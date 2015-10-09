"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

OJ's Binary Tree Serialization:

The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:

   1
  / \
 2   3
    /
   4
    \
     5

The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
"""
# Definition for a binary tree node.
#class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        # BFS
        retval = []
        queue = [root]
        is_reversed = False
        while len(queue) > 0:
            curr_level = []
            size = len(queue)
            for index in range(size):
                node = queue.pop(0)
                if not is_reversed:
                    curr_level.append(node.val)
                else:
                    curr_level.insert(0, node.val)

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

            is_reversed = (not is_reversed)
            if len(curr_level) > 0:
                retval.append(curr_level)

        return retval


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    tree = node1

    node1.left = node2
    node2.left = node3
    node3.left = node4
    node4.left = node5

    sol = Solution()
    print sol.zigzagLevelOrder(tree)
