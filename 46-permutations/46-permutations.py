class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        #base case 
        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            #pop the number in 0th index
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            #in python we can add more than 1 value in the arry
            result.extend(perms)
            nums.append(n)
        return result 
        