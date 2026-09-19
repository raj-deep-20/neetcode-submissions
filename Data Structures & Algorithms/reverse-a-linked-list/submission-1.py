# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next_tmp = curr.next
            curr.next = prev #reverse link 
            prev = curr # move prev fwd
            curr = next_tmp # move curr fwd
        return prev # the new head 