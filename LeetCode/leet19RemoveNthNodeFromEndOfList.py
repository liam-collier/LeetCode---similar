# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        while True:
            temp = curr
            for _ in range(n + 1):
                temp = temp.next
            if temp is None:
                curr.next = curr.next.next
                return dummy.next
            curr = curr.next