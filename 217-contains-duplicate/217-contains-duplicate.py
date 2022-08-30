class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for number in nums:
            if number in seen:
                return True 
            else:
                seen[number]=1
        return False
       
        
        
        
    '''
    seen = set()
        for number in nums:
            if number in seen:
                return True 
            else:
                seen.add(number)
        return False  
    '''        
        

        
        
        
        
                
        