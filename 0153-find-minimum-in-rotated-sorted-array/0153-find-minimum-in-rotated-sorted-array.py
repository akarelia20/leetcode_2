class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_num= nums[r]
        
        if len(nums) == 1:
            return nums[0]
        
        while r >= l:
            mid = (r+l)//2
            print(mid)
#             if mid is less than num at position r
            if nums[mid] < min_num:
                print(min_num)
                min_num = min(nums[mid], min_num) 
                print(min_num, nums[r], nums[mid] )
                r = mid -1
                
            else:
                l = mid +1
            

        return min_num
                
                
        