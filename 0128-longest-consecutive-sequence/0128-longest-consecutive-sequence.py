class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        length = 1
        for n in unique:
            i = 1
            while n-i in unique:
                i += 1
                length = i
            i = 1
            while n+i in unique:
                i += 1
                length = i
            longest = max(length, longest) 
            if longest == len(nums):
                break      
                
        return longest