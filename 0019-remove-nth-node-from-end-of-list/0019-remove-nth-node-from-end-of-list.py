# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy node is a copy of head listnode with 0 at the head and headnode in the head.next
        dummy = ListNode(0,head)
        slow = dummy
        fast = head
        
#        fast starts at the Nth position and slow starts at 0 at the dummy node
        while n >0:
            fast = fast.next
            n -= 1
            
        while fast:
            slow= slow.next
            fast = fast.next
        
        # Skipping nth node
        slow.next = slow.next.next
        return dummy.next
        