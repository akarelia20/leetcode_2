class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n-1]:
                continue
            l,r = n+1, len(nums)-1 
            while l < r:
                if (nums[n]+ nums[l] + nums[r]) > 0:
                    r -=1
                elif (nums[n]+ nums[l] + nums[r]) < 0:
                    l+= 1
                elif (nums[n]+ nums[l] + nums[r]) == 0:
                    res.append([nums[n], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
       
        return res
                
    