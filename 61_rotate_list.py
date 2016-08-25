"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    """
    Idea:
        - observe that, k is the number from tail to become head
        - in ex, k = 2, last 2nd element become head
        - two pointers, start, end, end = start + k + 1 away
        - run till end = null
        - new_head = start.next, start.next = null
        - traverse till the end, link tail -> old head
    """
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head

        # get the length
        curr = head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next

        if length == 1:
            return head

        k %= length
        if k == 0:
            return head

        start = head
        end = head
        while k >= 0:   # k + 1 away
            end = end.next
            k -= 1

        # traverse
        while end is not None:
            start = start.next
            end = end.next

        new_head = start.next
        start.next = None
        curr = new_head
        while curr.next is not None:
            curr = curr.next

        # link back to old head
        curr.next = head
        return new_head
