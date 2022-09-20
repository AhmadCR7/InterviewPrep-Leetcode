class Solution:
    def expandAndCountPali(self, i, j, s):
        strLength = len(s)
        cnt = 0 
        
        while i >= 0 and strLength > j and s[i] == s[j]:
            i -= 1 
            j += 1
            cnt += 1
        return cnt
    def countSubstrings(self, s: str) -> int:
        
        return sum(self.expandAndCountPali(i,i,s) + self.expandAndCountPali(i,i+1,s) for i in range(len(s)))
         
    
'''Counts the number of pallindrome substrings from a given center i,j        
        1. when i=j, it's an odd-lengthed pallindrome string. 
            eg: for string "aba", i=j=1.
        2. when i+1=j, it's an even-lengthed pallindrome string. 
            eg: for string "abba", i=1, j=2.
        
        Parameters:
            i,j - centers from which the code will expand to find number of pallindrome substrings.
            s - the string in which the code needs to find the pallindrome substrings. 
        
        Returns:
            cnt - The number of pallindrome substrings from the given center i,j       

**Time - O(len(s)^2)
Space - O(1)
**
        
'''