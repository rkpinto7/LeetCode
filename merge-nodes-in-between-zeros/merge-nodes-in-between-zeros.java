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
    public ListNode mergeNodes(ListNode head) {
        ListNode ans = new ListNode(0);
        ListNode dummy = ans;
        head = head.next;
        int sum = 0, addedVal = 0;
        while (head != null) {
            if (head.val == 0)
            {
                addedVal = sum;
                sum = 0;
                dummy.next = new ListNode(addedVal);
                dummy = dummy.next;
                
            } else sum += head.val;
            head = head.next;
        }
        return ans.next;
    }
}