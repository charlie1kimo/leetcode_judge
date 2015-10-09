/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        /*
         * Use Heap to solve. O(nlog(k))
         */
         if (lists == null || lists.length == 0) return null;
         
         Queue<ListNode> heap = new PriorityQueue(lists.length, new Comparator<ListNode>() {
            @Override
            public int compare(ListNode l1, ListNode l2) {
                return l1.val - l2.val;
            }}
         );
         for (ListNode n : lists) if (n != null) heap.add(n);
         
         ListNode dummy = new ListNode(0);
         ListNode tail = dummy;
         while (!heap.isEmpty()) {
             tail.next = heap.poll();
             tail = tail.next;
             if (tail.next != null) heap.add(tail.next);
         }
         return dummy.next;
    }
}