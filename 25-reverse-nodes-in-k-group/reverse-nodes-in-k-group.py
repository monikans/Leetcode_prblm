# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            count = 0
            curr = head
            while curr and count < k:
                curr = curr.next
                count += 1
            if count == k:
                new_head = curr
                prev_node = None
                curr_node = head
                for _ in range(k):
                    next_node = curr_node.next
                    curr_node.next = prev_node
                    prev_node = curr_node
                    curr_node = next_node
                head.next = new_head
                prev.next = prev_node
                prev = head
                head = head.next
            else:
                break
        return dummy.next