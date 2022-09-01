class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor operation 
        # r = [2,2,1]
        # r = (2^2)^(1)
        #   = 0 ^ 1 
        #   = 1
            
        res = 0 
        for n in nums:
            res = n ^ res 
        return res 
        
        
'''
we create a res 
go trough the array for n in nums
update the res res = n ^ res 
return res 
'''