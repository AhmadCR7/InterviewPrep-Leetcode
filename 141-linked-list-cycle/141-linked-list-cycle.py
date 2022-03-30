# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head 
        
        # we want to make sure fast and fast.next is not null if its the return False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True 
        return False 
    
    
    
    
    
    
    
    
    
        