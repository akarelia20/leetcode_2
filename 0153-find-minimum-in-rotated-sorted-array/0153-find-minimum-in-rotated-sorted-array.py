class Solution:
    def findMin(self, nums: List[int]) -> int:
        if sorted(nums) == nums:
            return nums[0]
      
        r= len(nums)-1
        l= 0
        min_num = nums[r]
        while r >= l:
            if nums[r] > min_num:
                break
            mid= (r+l)//2
            # if mid is  > than next element
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                min_num = min(nums[mid], min_num)
                r = mid-1
            print (min_num)
        return min_num
                
        