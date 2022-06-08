class Solution:
    def calculate(self, s: str) -> int:
        res = 0 
        sign = 1
        num = 0 
        stack = []
        
        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
            elif char in "+-":
                res += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif char == ")":
                res += sign * num 
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign 
        