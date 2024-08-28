/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *temp , *tail;
        temp = tail = head;
        while(temp!=NULL && temp->next !=NULL)
        {
            temp = temp->next->next;
            tail = tail->next;
            if(temp==tail)
            {
                return true;
            }
        }
        return false;
    }
};