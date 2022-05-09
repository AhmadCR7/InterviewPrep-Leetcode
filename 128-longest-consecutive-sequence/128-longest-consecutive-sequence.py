class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in numSet:
            if (n-1) not in numSet:
                lenght = 0
                while (n + lenght) in numSet:
                    lenght += 1
                longest = max(lenght, longest)
        return longest
            
    
    
    
    
# we create a set using our array 
#set nums = [100,4,200,1,3,2]
# we check if the 100 is the first element of the sequence 100 has no left number meaning there is no 99
# 100 ->  lenght 1
# 200 ->  lenght 1
# 1 -> 2 -> 3 -> 4  lenght 4
# time O(n) sicne we visit each elements once 
# Space: O(n) sicne we created a set() to see the size of an array