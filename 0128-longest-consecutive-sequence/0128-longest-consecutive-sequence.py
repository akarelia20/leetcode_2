class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # delcare set with all the uniequ values from num
        unique= set(nums)
        long = 0
        for i in nums:
            if (i-1) not in unique:
                length = 1
                while (i+length) in unique:
                    length += 1
                long = max(length, long)
        return long
            