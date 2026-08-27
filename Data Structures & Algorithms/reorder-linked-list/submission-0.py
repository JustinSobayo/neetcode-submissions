# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None

        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        current = head
        while prev:
            Lnxt = current.next
            Rnxt = prev.next
            current.next = prev
            prev.next = Lnxt
            current = Lnxt
            prev = Rnxt
        




