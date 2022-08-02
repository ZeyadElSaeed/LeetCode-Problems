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
        
        ListNode first = head;
        ListNode second = head;
        
        for ( int i=1; i<=n; i++){
            first = first.next;
        }
        
        if ( first == null )return head.next;
        
        while ( first.next != null ){
            first = first.next;
            second = second.next;
        }
        ListNode temp = second.next;
        second.next = temp.next;
        return head;
        
        
        
            
    }
}