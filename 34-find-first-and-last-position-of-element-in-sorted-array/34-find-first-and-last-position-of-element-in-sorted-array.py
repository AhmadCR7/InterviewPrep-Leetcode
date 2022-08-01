class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        
        """
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]
    def binarySearch(self, nums, target, leftBais):
        l, r = 0, len(nums) - 1
        i = -1
        while(l <= r):
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                i = mid 
                if leftBais:
                    r = mid - 1
                else:
                    l = mid + 1
        return i 
        
                        
                    
        