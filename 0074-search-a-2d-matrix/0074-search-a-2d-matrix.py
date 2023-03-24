class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
#         binary search to find which row the number exsist
        top_row, bot_row = 0, len(matrix)-1 
        while top_row <= bot_row:
            mid_row= (top_row+bot_row)//2
            if target > matrix[mid_row][-1]:
                top_row = mid_row +1
            elif target < matrix[mid_row][0]:
                bot_row = mid_row-1
            else:
                break
                
        if not (top_row <= bot_row):
            return False
        
        # once we know which row the number might exsist - binary seach again to see if it is present
        row = (top_row + bot_row)//2
        l, r = 0, len(matrix[0])-1
        
        while l <= r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m +1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        
        return False
                
            
                