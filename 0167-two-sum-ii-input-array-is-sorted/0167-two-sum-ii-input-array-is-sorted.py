class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        output = []
        for i in range(len(nums)):
            if target-nums[i] in dict:
                output.append(dict[target-nums[i]]+1)
                output.append(i+1)
            dict[nums[i]] = i
            print(dict, output)
        return output
                