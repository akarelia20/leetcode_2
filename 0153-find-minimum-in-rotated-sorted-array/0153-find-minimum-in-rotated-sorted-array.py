class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_num= nums[r]
        
        while r >= l:
#        min is found
            if min_num < nums[r]:
                break
            mid = (r+l)//2
#         left half of the arr has min
            if nums[mid] < min_num:
                min_num = min(nums[mid], min_num) 
                r = mid -1
#         right half of the arr has min
            else:
                l = mid +1            

        return min_num
                
                
        