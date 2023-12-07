# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = ListNode(0, head)
        curr = dummy
        while curr is not None and curr.next is not None:
            if curr.next.next is None:
                curr = None
            else:
                temp = curr.next
                curr.next = curr.next.next
                temp2 = curr.next.next
                curr.next.next = temp
                temp.next = temp2
                curr = curr.next.next
        return dummy.next