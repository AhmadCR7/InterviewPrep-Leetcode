class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1
        while low <= high:
            midRow = (low + high)//2
            row = matrix[midRow]
            if target < row[0]:
                high = midRow -1
            elif target > row[-1]:
                low = midRow + 1
            else:
                l, r = 0, len(row)-1
                while l<= r:
                    mid = (l+r)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False 
        
        
        
        
        
        
        
        
        
        
       
        
                
        
                

            
            
            
            
            
