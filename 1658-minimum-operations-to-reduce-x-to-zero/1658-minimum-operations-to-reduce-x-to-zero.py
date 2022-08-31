class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        current = sum(nums)
        l = 0
        mini = inf
        
        
        for r in range(len(nums)):
            current -= nums[r]
            while current < x and l <= r:
                current += nums[l]
                l += 1
            if current == x:
                mini = min(mini, (len(nums)-1-r)+ l)
        return mini if mini != inf else -1
                