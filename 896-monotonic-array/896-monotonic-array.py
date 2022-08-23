class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a = sorted(nums)
        b = sorted(nums, reverse = True)
        if nums == a or nums == b:
            return True
        return False 
        
        
        
'''
a = sorted(nums)
        b = sorted(nums,reverse=True)
        if nums == a or nums == b:
            return True
        return False
'''
        
        
        