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
    public ListNode oddEvenList(ListNode head) {
        ListNode o=head;
        ListNode e=head.next,ev=e;
        while(e!=null && e.next!=null){
            o.next=e.next;
            o=o.next;
            e.next=e.next.next;
            e=e.next;

        }
        o.next=ev;
        return head;

    }
}