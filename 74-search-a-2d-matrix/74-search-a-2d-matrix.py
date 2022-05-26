class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        
        top, btm = 0, ROW - 1
        while top <= btm:
            #find the middle row
            row = (top + btm) // 2
            #look at the left most value 
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                btm = row - 1
            else:
                break 
        if not(top <= btm):
            return False 
        row = (top + btm) // 2
        l, r = 0, COL - 1
        while l <= r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True 
        return False 
                
        
                
        
        