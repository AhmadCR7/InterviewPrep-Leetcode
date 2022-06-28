class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0
        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSub = max(currSum, maxSub)
        return maxSub
        

    '''
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
         -1, -3 we dont use them 
                3,2,1 = 6 answer 
    '''