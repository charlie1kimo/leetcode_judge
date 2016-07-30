"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
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
    def addTwoNumbers(self, l1, l2):
        head = None
        curr_node = None
        carry_on = 0
        while l1 != None or l2 != None:
            sum_val = 0
            if l1 != None:
                sum_val += l1.val
                l1 = l1.next
            if l2 != None:
                sum_val += l2.val
                l2 = l2.next
            sum_val += carry_on
            new_node = ListNode(sum_val % 10)
            carry_on = sum_val / 10
            if curr_node == None:
                curr_node = new_node
                head = curr_node
            else:
                curr_node.next = new_node
                curr_node = new_node
        
        if carry_on > 0:
            new_node = ListNode(carry_on)
            curr_node.next = new_node
            
        return head
                