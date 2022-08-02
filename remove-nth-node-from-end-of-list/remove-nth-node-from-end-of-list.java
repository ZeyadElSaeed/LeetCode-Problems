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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if ( head == null ) return null;
        ListNode res;
        
        int size = 0;
        ListNode node = head;
        while ( node != null ){
            size++;
            node = node.next;
        }
        
        int index = size - n;
        if ( index == 0 ){return head.next;}
        ListNode curr = head; 
        ListNode prev = null; 
        
        while ( index > 0 ){
            prev = curr;
            curr = curr.next;
            index-=1;
        }
        
        prev.next = curr.next;
        curr.next = null;
        return head;
            
    }
}