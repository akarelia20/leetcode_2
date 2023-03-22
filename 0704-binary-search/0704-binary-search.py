class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        
        while r >= l:
            mid = l+(r-l)//2
            print(mid, r,l)
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] == target:
                return mid 
        return -1
        