class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
        
'''
x=Counter(ransomNote)
        y=Counter(magazine)
        for i,v in x.items():
            if(x[i]<=y[i]):
                continue
            else:
                return False
        return True
'''