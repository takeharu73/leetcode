# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_new = head
        while True:
            if head == None or head.next == None:
                break
            elif head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next                
                
        return head_new

    """
    1,1,2
    head = 1 head.next = 1  [1,1,2]
            head.next = 2   [1,2]
            
    1,1,2,3,3
    head = 1 head.next = 1   [1,1,2,3,3]
            head.next = 2   [1,2,3,3]
    head = 1 head.next = 2   [1,2,3,3]  
    head = 2 head.next = 3   [1,2,3,3]
    head = 3 head.next = 3   [1,2,3,3]
    head = 3 head.next = None   [1,2,3]
    """