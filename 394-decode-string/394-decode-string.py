class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            #we want to check if it's not a closing bracket 
            if s[i] !="]":
                stack.append(s[i])
            # what if we do fine a closing bracket
            else:
                substr = ""
                # while the top of the stack is not equal to closing bracket we keep poping
                while stack[-1] != "[":
                    substr = stack.pop() +substr
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * substr)
    
        return "".join(stack)
        
                    
                
                
        