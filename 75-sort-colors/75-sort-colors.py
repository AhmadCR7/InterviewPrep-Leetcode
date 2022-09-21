class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = curr = 0
        p2 = len(nums)-1
        
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1
'''
Algorithm
Initialise the rightmost boundary of zeros : p0 = 0. During the algorithm execution nums[idx < p0] = 0.

Initialise the leftmost boundary of twos : p2 = n - 1. During the algorithm execution nums[idx > p2] = 2.

Initialise the index of current element to consider : curr = 0.

While curr <= p2 :

If nums[curr] = 0 : swap currth and p0th elements and move both pointers to the right.

If nums[curr] = 2 : swap currth and p2th elements. Move pointer p2 to the left.

If nums[curr] = 1 : move pointer curr to the right.

Complexity Analysis

Time complexity : \mathcal{O}(N)O(N) since it's one pass along the array of length NN.
Space complexity : \mathcal{O}(1)O(1) since it's a constant space solution.
'''
                
        