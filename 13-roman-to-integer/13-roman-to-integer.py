class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        
        res = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res
        
        
'''
Solution: 
we use hashmap to map through the string 
we go throgh the string for i in range(len(s))
now we check are we substraction the if i + 1 < len(s) we don't want to be out of bound 
and check what is the value at index[i] we can check that from roman[s[i]] and check if that 
value is smaller than the next char roman[s[i+1]]
if its less than that we subtract it res -= roman[s[i]]
if not add else: res += roman[s[i]]
return the result 

'''