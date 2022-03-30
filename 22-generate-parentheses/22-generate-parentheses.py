class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        
        def backtrack(openN, closeN):
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
            if openN == closeN == n:
                res.append("".join(stack))
        backtrack(0,0)
        return res
        
        
        
        
        
        
        
        

         