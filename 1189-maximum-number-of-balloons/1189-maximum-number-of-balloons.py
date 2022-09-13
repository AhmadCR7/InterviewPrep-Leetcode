class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = {'a':0, 'b':0,'l':0, 'n':0, 'o':0}
        double_char = ['l','o']
        for c in text:
            if c in word:
                word[c] += 1
        for c in double_char:
            word[c] //= 2
        return min(word.values())
            
            

        
        
        
'''
A Counter is a container that keeps track of how many times equivalent values are added.
counter = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for char in text:
            if char in counter:
                counter[char] += 1
        counter["l"] //= 2
        counter["o"] //= 2
        return min(counter.values())
Intuitive Python Solution with O(n) time and O(1) space.


'''