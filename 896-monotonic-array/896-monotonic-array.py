class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a = sorted(nums)
        b = sorted(a, reverse = True)
        if nums == a or nums == b:
            return True
        return False 
        
        

        
        
        