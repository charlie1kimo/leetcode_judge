"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """
    Idea:
        (1) top-down approach:
            - Time: O(nlog(n)) (because we need to walk through to calculate the length)
            - keep track of head and tail
            - calculate mid, then pass in left list and right list
            - recursively build subtrees
        (2) bottom-up approach:
            - Time: O(n)
            - allocate dummy node
            - go left with n/2 nodes
            - set dummy.val = curr.val
            - go right with (n - n/2 - 1) nodes (total - left - root)
    """
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None

        self.curr = head

        return self.sortedListToBST_recursive_bottom_up(self.length_of_linked_list(head))

    def length_of_linked_list(self, head):
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    def sortedListToBST_recursive_bottom_up(self, n):
        if n == 0:
            return None

        node = TreeNode(0)
        node.left = self.sortedListToBST_recursive_bottom_up(n / 2)
        node.val = self.curr.val
        self.curr = self.curr.next
        node.right = self.sortedListToBST_recursive_bottom_up(n - n / 2 - 1)
        return node

    def sortedListToBST_top_down(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None

        curr = head
        while curr.next is not None:
            curr = curr.next
        tail = curr

        return self.sortedListToBST_recursive_top_down(head, tail)

    def sortedListToBST_recursive_top_down(self, head, tail):
        # base case
        if head is None or tail is None:
            return None

        length = 1  # inclusive head == tail
        curr = head
        while curr is not None and curr != tail:
            length += 1
            curr = curr.next

        mid = length / 2
        steps = mid
        prev = None
        curr = head
        while steps > 0:
            prev = curr
            curr = curr.next
            steps -= 1

        right_start = None if curr == tail else curr.next
        root = TreeNode(curr.val)
        # non-leaf node
        root.left = self.sortedListToBST_recursive(head, prev)
        root.right = self.sortedListToBST_recursive(right_start, tail)

        return root
