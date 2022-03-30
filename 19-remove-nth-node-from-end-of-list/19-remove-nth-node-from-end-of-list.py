# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # keep shifiting the right to the end of the nodeonce n = 0 is when that all we wanted 
        
        while n > 0 and right:
            right = right.next 
            n -= 1
        #once the right is at the end the left pointer will be at the node we want to delete 
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next 
            

        
# head = [1,2,3,4,5]
# dummy = [0,1,2,3,4,5]
# left = dymmy
# right = head
# n = 2
# keep shifting until the right is at null and left will be at the node we want to delete 
# time complxity is O(n)








        
        
        
        
        
        
        
        
        
        
        
        
        
        
        