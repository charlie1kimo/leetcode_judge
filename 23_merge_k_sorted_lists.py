"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. 
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    idea:
        divide and conquer
        Time: O(nlog(k))
    """
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) / 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        head = None
        curr = None
        while left != None or right != None:
            if left == None:
                if head == None:
                    head = right
                    curr = right
                    right = right.next
                else:
                    curr.next = right
                    curr = right
                    right = right.next
                    curr.next = None
            elif right == None:
                if head == None:
                    head = left
                    curr = left
                    left = left.next
                else:
                    curr.next = left
                    curr = left
                    left = left.next
                    curr.next = None
            elif left.val > right.val:
                if head == None:
                    head = right
                    curr = right
                    right = right.next
                else:
                    curr.next = right
                    curr = right
                    right = right.next
                    curr.next = None
            else:
                if head == None:
                    head = left
                    curr = left
                    left = left.next
                else:
                    curr.next = left
                    curr = left
                    left = left.next
                    curr.next = None
        return head


