class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left , right = 0,len(nums)
        while left < right:
            mid = (left+right)//2
            # find the leftest number that is lower than the nums[-1]
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid+1
        return nums[left]
        