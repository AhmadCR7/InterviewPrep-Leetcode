class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right, pInx):
            pivot = nums[pInx]
            nums[pInx], nums[right] = nums[right], nums[pInx]
            
            storeIndex = left
            
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[storeIndex], nums[i] = nums[i], nums[storeIndex]
                    storeIndex += 1
            
            nums[right], nums[storeIndex] = nums[storeIndex], nums[right]
            
            return storeIndex
        
        def select(left, right, k_smallest):
            if left == right:
                return nums[left]
            pInx = random.randint(left, right)
            pInx = partition(left, right, pInx)
            if k_smallest == pInx:
                return nums[k_smallest]
            elif k_smallest < pInx:
                return select(left, pInx - 1, k_smallest)
            else:
                return select(pInx + 1, right, k_smallest)
        return select(0, len(nums)-1, len(nums) - k)
    
    
    
    
'''
solution 1:
nums.sort()
return nums[-k]

time: O(nNlogk)
Space: O(K) to store heap elements 

'''