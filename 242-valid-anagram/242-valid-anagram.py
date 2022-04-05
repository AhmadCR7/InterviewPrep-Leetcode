class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        
# you can also use built in function of return Count(s) == Count(t)