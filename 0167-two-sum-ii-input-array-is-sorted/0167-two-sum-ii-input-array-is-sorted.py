class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1
        
        while l<r:
            sum= nums[l]+ nums[r]
            if sum>target:
                r -=1
            if sum<target:
                l +=1
            if sum == target:
                return [l+1, r+1]