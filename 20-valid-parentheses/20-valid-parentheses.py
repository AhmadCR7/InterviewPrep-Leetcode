class Solution:
    def isValid(self, s: str) -> bool:
        # we use hashmap to match if close parentheses matches with open one 
        # we create stack on top to match them
        # we repeat this process until our stack is empty and we match all the {} 
        # the time complexity is O(n) since we got to each input charactor once 
        # memory use will be O(n) sice we use the size of stack 
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{" }

        # go throgh every input charactor 
        for char in s: 
            if char in closeToOpen: # check if this charactor is closing prantices (bc all the charctor are key) 
                if stack and stack[-1] == closeToOpen[char]: # find the open one on top of the stack and match them 
                    stack.pop()
                else: 
                    return False 
            else:
                stack.append(char) ## add as many as pranteses you want
        # return true only if the stack is empty 
        return True if not stack else False
        
        
        
        
    
       
      
            
    
    

                
                    
                
            
                
            
        