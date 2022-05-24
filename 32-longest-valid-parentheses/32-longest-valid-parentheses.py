class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0 
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif len(stack) == 1:
                stack[0] = i
            else:
                stack.pop()
                ans = max(ans, i-stack[-1])
        return ans
        