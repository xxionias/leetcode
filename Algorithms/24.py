# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 1. edge case
        if not head or not head.next:
            return head

        # 2. set two pointers and prev
        dummy = ListNode(val=-1, next=head)
        prev = dummy

        # 3. swap the values
        while head and head.next:
            ptr1, ptr2 = head, head.next

            ptr1.next = ptr2.next
            ptr2.next = ptr1
            prev.next = ptr2

            prev = ptr1
            head = head.next

        return dummy.next
