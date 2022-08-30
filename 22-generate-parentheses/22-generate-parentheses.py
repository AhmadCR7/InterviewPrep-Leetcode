class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(openN, closedN): 
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res 

    
    
        
        
        
'''
Solution using stack: 

1. N = 3
We need 3 open and 3 close parentheses
Rules: - 3 open, 3 close and close < open 
#only add open parentheses if open < n
#only add a closing parentheses if closed < open 
#valid IIF open == closed == n


def backtrack(openN, closedN): 
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res 


'''
        
        

         