class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res 
            
'''
we create a charSet = set()
we do sliding window to we use leftP = 0 and right changes as we go for r in range(len(s)):
if we get to duplicate we update the window in our set while s[r] in charSet:
we have to remove it for the charSet.remove(s[leftP])
update the pointer leftP += 1
the add the right most char to our set charSet.add(s[r])
now update our result res = max(res, r-leftP+1)
retturn res 

Time: o(n) we go throgh the set by adding and removing 
Space: o(n) becuase of the set since they can be unique 



'''
        
        