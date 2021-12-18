# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        else:
            while True:
                if head.next is None:
                    return False
                elif head.val is None:
                    return True
                else:
                    head.val = None
                    head = head.next