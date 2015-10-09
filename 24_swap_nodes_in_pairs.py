"""
 Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    idea:
        3 pointers:
        curr, first, second
        curr->first->second
        curr.next = second
        first.next = second.next
        second.next = first

        curr = first
        first = curr.next
        second = first.next
    """
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        first = head
        second = head.next
        while second != None:
            curr.next = second
            first.next = second.next
            second.next = first

            curr = first
            first = curr.next
            if first == None:
                second = None
            else:
                second = first.next

        return dummy.next
