/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        while ( headB != null ){
            ListNode node = headA ;
            while ( node != null ){
                if ( node == headB ) return node;
                node = node.next;       
            }
            headB = headB.next;
        }
        return null ;
            
        
    }
}