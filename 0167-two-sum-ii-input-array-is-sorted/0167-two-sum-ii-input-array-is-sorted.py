class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for i in range(len(nums)):
            if target-nums[i] in dict:
                output=[(dict[target-nums[i]]+1),(i+1)]
            dict[nums[i]] = i
        return output
                