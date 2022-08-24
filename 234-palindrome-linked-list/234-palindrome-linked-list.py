# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        stack = []
        isPlain = True
        # Push all elements of the list
        # to the stack
        while slow != None:
            stack.append(slow.val)
            # move the head
            slow = slow.next
            
        while head != None:
            i = stack.pop()
            
            if head.val == i:
                isPlain = True 
            else:
                isPlain = False
                break
                 
            head = head.next
        return isPlain
            
            