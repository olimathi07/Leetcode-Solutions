/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode h) {
      if (h==null)return false;
      ListNode i=h;
      ListNode j=h.next;
      while(i!= null && j!= null){
        if(i==j)
            return true;
            i=i.next;
            j=j.next.next;
        
        
        
      }   
        return false;
        
    }
}