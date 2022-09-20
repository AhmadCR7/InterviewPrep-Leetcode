class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        sets = set()
        for char in s:
            if char not in sets:
                sets.add(char)
            else:
                sets.remove(char)
        return (len(sets) <= 1)
        
        

'''     
 # Set: Iterate over the given string
    # Add the character when it is not there, Remove it when it is.
    # At the end, the length of the sets is lesser than 2
    # TC O(n) n is the number of the character of string
    # SC O(1) the maximum size of the set would be 128 ASCII characters
    # This is bounded (constant),
    def canPermutePalindrome(self, s: str) -> bool:
        sets = set()
        for char in s:
            if char not in sets:
                sets.add(char)
            else:
                sets.remove(char)
        
        return (len(sets) <= 1)  
'''