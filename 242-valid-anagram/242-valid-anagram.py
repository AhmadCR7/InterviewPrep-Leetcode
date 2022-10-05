class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)
        dic1, dic2 = [0] * 26, [0] * 26

        for item in s:
            dic1[ord(item) - ord('a')] += 1
        for item in t:
            dic2[ord(item) - ord('a')] += 1
        return dic1 == dic2
        
        
# you can also use built in function of return Count(s) == Count(t)