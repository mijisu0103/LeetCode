# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            a, b = 0, 0
            if l1:
                a, l1 = l1.val, l1.next
            if l2:
                b, l2 = l2.val, l2.next

            carry, val = divmod(a + b + carry, 10)
            ret.next = ListNode(val)
            ret = ret.next

        return head.next