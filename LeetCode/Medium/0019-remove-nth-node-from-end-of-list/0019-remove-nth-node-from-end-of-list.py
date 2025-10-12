# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head

        firstPtr = secondPtr = dummy

        for _ in range(n):
            firstPtr = firstPtr.next

        while firstPtr and firstPtr.next:
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next

        secondPtr.next = secondPtr.next.next

        return dummy.next