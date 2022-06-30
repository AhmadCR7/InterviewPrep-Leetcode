# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head 
        dummy = ListNode(0, next = head)
        prev = dummy 
        i = 1
        while i < left:
            prev = prev.next
            i += 1
        curr = prev.next
        nxt = curr.next 
        
        while i < right:
            tmp = nxt.next 
            nxt.next = curr
            curr = nxt
            nxt = tmp 
            i += 1
        prev.next.next = nxt
        prev.next = curr
        
        return dummy.next 
         
            
            
        