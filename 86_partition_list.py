"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    """
    Idea:
        - two partitioned lists with small than & greater or equal to than
        - then concatenate to lists
    """
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # dummy starts
        small_head = ListNode(0)
        small = small_head
        big_head = ListNode(0)
        big = big_head

        curr = head
        while curr is not None:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                big.next = curr
                big = big.next
            curr = curr.next

        # concatenation
        big.next = None
        small.next = big_head.next
        return small_head.next
