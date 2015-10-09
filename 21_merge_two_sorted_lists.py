"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head = curr = None

        while l1 != None or l2 != None:
            node = None
            if l1 == None:
                node = l2
                l2 = l2.next
            elif l2 == None:
                node = l1
                l1 = l1.next
            elif l1.val <= l2.val:
                 node = l1
                 l1 = l1.next
            else:
                node = l2
                l2 = l2.next

            if head == None:
                head = node
                curr = node
            else:
                curr.next = node
                curr = curr.next

        return head
