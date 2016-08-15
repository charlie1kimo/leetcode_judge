"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr is not None:
            # skip
            while curr.next is not None and curr.val == curr.next.val:
                curr = curr.next

            # deletion
            if prev.next != curr:
                prev.next = curr.next
            else:
                prev = curr

            # move the ptr forward
            curr = curr.next

        return dummy.next
