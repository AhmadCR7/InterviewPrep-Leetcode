class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {")" : "(", "]" : "[", "}" : "{" }
        
        for char in s:
            if char in openToClose:
                if stack and stack[-1] in openToClose[char]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(char)
        return True if not stack else False 
            
        
        
'''

Solution using hashnap 
 # we use hashmap to match if close parentheses matches with open one 
        # we create stack on top to match them to match a closing parenthesis to the open one 
        # we repeat this process until our stack is empty and we match all the {} 
        # the time complexity is O(n) since we got to each input charactor once 
        # memory use will be O(n) sice we use the size of stack 
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{" }

'''
    
       
      
            
    
    

                
                    
                
            
                
            
        