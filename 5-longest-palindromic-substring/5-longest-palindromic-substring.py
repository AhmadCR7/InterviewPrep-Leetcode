class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longestStr = 0
        
        for i in range(len(s)):
            #odd lenght palindroms 
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #if the lenght is greater then the current 
                if (r - l + 1) > longestStr:
                    res = s[l:r+1]
                    longestStr = r - l + 1
                l -= 1
                r += 1
            # Even Lenght Palindroms 
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #if the lenght is greater then the current 
                if (r - l + 1) > longestStr:
                    res = s[l:r+1]
                    longestStr = r - l + 1
                l -= 1
                r += 1
        return res
        
        
                    
        
        
        
        
        
'''
p = ''
        for i in range(len(s)):
            p1 = self.get_palindrome(s, i, i+1)
            p2 = self.get_palindrome(s, i, i)
            p = max([p, p1, p2], key=lambda x: len(x))
        return p
    
    def get_palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
        
         res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]
'''