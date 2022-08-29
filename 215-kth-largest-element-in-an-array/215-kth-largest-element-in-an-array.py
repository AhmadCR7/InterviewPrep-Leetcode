class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickselect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k: return quickselect(l, p - 1)
            elif p <k: return quickselect(p+1, r)
            else:      return nums[p]
        return quickselect(0, len(nums)-1)
                
    
    
    
'''
solution 1:
nums.sort()
return nums[-k]

time: O(nNlogk)
Space: O(K) to store heap elements 

Solution 2: 
QuickSelect Algo

[3,2,1,5,6,4]

pivet = [4]
[3,,,,,,]
sift the p
[3,2,1,5,6,4] the left side of the array is less than the pevit 
swap the p with the pevit 
[3,2,1,4,6,5]

now lenght - k run quick sort on the right side 

[3,2,1,4,5,6]

'''