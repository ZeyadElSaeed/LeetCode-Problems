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
    public ListNode rotateRight(ListNode head, int k) {
        if ( head == null ) return head;
        ListNode curr = head;
        int size = 1;
        while ( curr.next != null ){
            curr = curr.next;
            size++;
        }
         
        k = k % size;
        if ( k == 0) return head;
        else{
            ListNode endNode = head;
            for(int i =1; i < (size - k); i++ )
                endNode = endNode.next;
            curr.next = head;
            head = endNode.next;
            endNode.next = null;
            return head;
        }
    }
}