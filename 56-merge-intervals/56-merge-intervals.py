class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
            
        
        
        
        
'''
we want to sort the interval based on the start value 
then iterate through each start value 
we check if the current interval overlap with previous interval 
if it does we merge them in one interval 

intervals.sort(key = lambda i : i[0]) sort the interval 
the key is gonna be a lambda function where i stands for interval and i[0] is sort by start val
output = [intervals[0]] the merged at the end 

now we go through the interval in sorted order for start, end in intervals[1:]: except the first interval 

how to we know if they are overlapping? we can get the most recently added and it's value 
lastEnd = output[-1][1]

if start <= lastEnd: if they overlapping 
merge them output[-1][1] = max(lastEnd, end)
else: 
    output.append([start, end ]) if they are not over lapping just return itself 
return output 


time: O(nlogn) since we sort the intervals that we are given 


'''