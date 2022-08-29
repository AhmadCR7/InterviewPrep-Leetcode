class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)
        
        
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