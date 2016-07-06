"""
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5 
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    Idea:
        - run the linked-list only once, reverse as it goes.
        - O(n)
        - use a sentinel (dummy node)
    """
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        if k == 1:
            return head

        # sentinel node
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        curr = head
        while curr != None:
            new_head = prev.next
            group = k
            while new_head != None and group > 0:
                group -= 1
                new_head = new_head.next

            # end of the list
            if group > 0:
                break

            # note curr.next
            while curr.next != new_head:
                nt = curr.next.next
                # reversing curr & curr.next
                curr.next.next = prev.next
                prev.next = curr.next
                # linking the list back
                curr.next = nt
                # prev
                #   x    curr   x
                #   x     x     x   nt
            prev = curr
            curr = curr.next

        return dummy.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    Idea:
        - can reduce the problem to reverse a singly-linked list
        - reverse a singly-linked list with 3 pointers:
            1) 1->2->3->4->5        prev, curr, next
            2) 1<-2  3->4->5
            3) 1<-2<-3  4->5
            4) 1<-2<-3<-4  5
            5) 1<-2<-3<-4<-5
        - get k for tail from curr, then reverse. If nodes # < k no changes.

    Notes:
        - O(n + n % k) solution, which is not fast enough for the first try
    """
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        if k == 1:
            return head

        curr = head
        tail = head
        while tail != None:
            counter = 0
            while counter < k-1:
                if tail.next == None:
                    break
                tail = tail.next
                counter += 1

            # perform reverse
            if not counter < k-1:
                mid_head = self.reverseList(curr, tail)
                if curr == head:
                    head = mid_head

                # reversed pointer...
                curr = curr.next
                tail = curr
        return head

    def reverseList(self, head, tail):
        """
        @purpose:
            reverse singly-linked list from head to tail
        @returns:
            (ListNode) new head
        """
        # length 1, no change.
        if tail == None and head.next == None:
            return head

        prev = head
        curr = head.next
        next = head.next.next

        head.next = tail.next
        while curr != tail:
            curr.next = prev
            prev = curr
            curr = next
            if next != None:
                next = next.next

        tail.next = prev
        return tail
