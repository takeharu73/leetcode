# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        val_l = []
        node = head
        while True:
            val_l.append(node.val)
            node = node.next
            if node is None:
                break
        i = 0
        node = head        
        while True:
            node.val = val_l[-(i+1)]
            node = node.next
            i += 1
            if node is None:
                break
            
        return head
        