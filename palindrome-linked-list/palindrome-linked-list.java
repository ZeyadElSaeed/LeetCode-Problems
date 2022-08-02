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
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null ) return true;
        ListNode curr = head;
        int size = 1;
        
        while ( curr.next != null ){
            curr = curr.next;
            size++;
        }
        
        int count;
        if ( size % 2 == 0 )count = size/2;
        else count = size/2 + 1;
        
        curr = head;
        for ( int i=1; i< count; i++)
            curr = curr.next;
        
        curr.next = reverse( curr.next );
        ListNode second = curr.next;
        ListNode first = head;
        while ( second != null ){
            if (second.val != first.val ) return false;
            second = second.next;
            first = first.next;
        }
        return true ;
        
    }
    
    public ListNode reverse( ListNode node ){
        if ( node == null || node.next == null ) return node;
        
        ListNode rest = reverse( node.next );
        node.next.next = node;
        node.next = null;
        
        return rest;

    }
}