/*
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || head.next == null || left == right) return head; 

        ListNode dummy = new ListNode(0);
        dummy.next = head;
            
        // find node_m and node_m -1
        ListNode node_m_minus = dummy;
        for (int i = 0; i < left - 1; i++) {
            node_m_minus = node_m_minus.next;
        }
        ListNode node_m = node_m_minus.next;
        
        // find node_n and node_n + 1
        ListNode node_n = dummy;
        for (int i = 0; i < right; i++) {
            node_n = node_n.next;
        }
        ListNode node_n_plus = node_n.next;
        
        node_m_minus.next = null;
        node_n.next = null;
        while (node_m != null) {
            ListNode temp = node_m;
            node_m = node_m.next;
            temp.next = node_n_plus;
            node_n_plus = temp;
        }
        node_m_minus.next = node_n_plus;
        
        return dummy.next;
    }
}
