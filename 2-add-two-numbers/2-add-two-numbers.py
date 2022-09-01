# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy 
        
        carry = 0
        # while ls and ls are not null 
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 
         # the new digit  
            val = v1 + v2 + carry
        # for the reminder more than 1 digit like 15
            carry = val // 10 
            val = val % 10 
        # now that we add them we add it to list node 
            curr.next = ListNode(val)
        
        #update the pointer 
            curr = curr.next
        # update l1 an l2 pointer 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 

        return dummy.next
        
        
        
            
            
            
        
        
        