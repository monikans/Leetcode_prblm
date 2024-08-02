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
    public ListNode detectCycle(ListNode head) {
        ListNode temp = head;
        ListNode tail = head;
        while(temp!=null && temp.next!=null)
        {
            temp = temp.next.next;
            tail = tail.next;
            if(temp==tail)
            {
                ListNode curr = head;
                int pos=0;
                while(curr!=tail)
                {
                    curr = curr.next;
                    tail = tail.next;
                    pos++;
                }
                System.out.println("tail connects to node index "+ pos);
                return curr;
            }
        }
    return null;
    }
}