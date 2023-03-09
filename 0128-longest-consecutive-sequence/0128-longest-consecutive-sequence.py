class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        remove= set()
        longest = 0
        for n in unique:
            length =1
            if n not in remove:
            
                i = 1
                while n-i in unique:
                    i += 1
                    length += 1
                    remove.add(n-i)
                i = 1
                while n+i in unique:
                    i += 1
                    length += 1
                    remove.add(n+i)
            
            longest = max(length, longest) 
            remove.add(n)
            # if longest == len(nums):
            #     break      
                
        return longest
            