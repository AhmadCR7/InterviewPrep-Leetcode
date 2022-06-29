# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        oddptr = curr = head
        evenptr = overhead = head.next
        i = 1
        
        while curr:
            if i > 2 and i % 2 != 0:
                oddptr.next = curr
                oddptr = oddptr.next 
            elif i > 2 and i % 2 == 0:
                evenptr.next = curr
                evenptr = evenptr.next 
            curr = curr.next 
            i += 1
        evenptr.next = None 
        oddptr.next = overhead
        return head 
'''
1. first we check if there is head 
2. check if there is one node 
3. check if there is odd node
4. we set up and index numbder to see if we are in even or odd number 
5. we don't care about first and second since we already point the pointers at them 
6. 
'''
                
            
        
        
        