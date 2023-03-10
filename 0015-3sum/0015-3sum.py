class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique = set()
        res = []
        
        for n in range(len(nums)):
            l,r = n+1, len(nums)-1 
            while l < r:
                if (nums[n]+ nums[l] + nums[r]) > 0:
                    r -=1
                elif (nums[n]+ nums[l] + nums[r]) < 0:
                    l+= 1
                elif (nums[n]+ nums[l] + nums[r]) == 0:
                    y = "".join(str(j) for j in [nums[n], nums[l], nums[r]])
                    if y not in unique:
                        res.append([nums[n], nums[l], nums[r]])
                    unique.add(y)
                    r -= 1
                    l += 1
#                     prevents duplicate entries in res array
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
       
        return res
                
    