class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        dict= {}
        longest = 0
        length = 1
        for n in unique:
            i = 1
            dict[n] = length
            while n-i in unique:
                i += 1
                length = i

            i = 1
            while n+i in unique:
                i += 1
                length = i
            dict[n] = length
            
            longest = max(length, longest)
            
            if longest == len(nums):
                break      
                
        return longest
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
#         unique= set(nums)
#         long = 0
#         for i in nums:
#             if (i-1) not in unique:
#                 length = 1
#                 while (i+length) in unique:
#                     length += 1
#                 long = max(length, long)
#         return long
            