class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        output, mul = 0, 0
        
        for i, p in enumerate(s):
            if p == '(':
                mul += 1
            elif p == ')':
                mul -= 1
                
                if i > 0 and s[i - 1] == '(':
                    output += 2**mul
        return output