class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)
        
               
        
        
# Solution One:        
# we build hasmap "element --> frequency"
# [1,1,1,2,2,2,3,3,4,5,5,5,5]
# 1 -> 3
# 2 -> 3
# 3 -> 2
# 4 -> 1
# 5 -> 4
# build min heap of k most frequent elements 
# 1 2 5
# build an output array 
# [2,5,1]
# Time: O(nlonk)
# SP: O(N + K)
'''
if k == len(nums):
            return nums
        # # 1. build hash map : character and how often it appears
        count = Counter(nums)
        # # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        
        return heapq.nlargest(k, count.keys(), key = count.get)
'''

#Solution 2: 
