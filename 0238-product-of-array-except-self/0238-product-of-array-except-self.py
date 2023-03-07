class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x =1
        result= []
        
        for j in range(len(nums)):
            if j == 0:
                result.append(x)
            else:
                result.append(result[j-1] * nums [j-1])
        
        for i in range(len(nums)-1,-1,-1):
            result[i] = result[i] * x 
            x = x * nums[i]
            
        return result
            