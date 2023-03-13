class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         solving using sliding window r,l pointers
        char= set()
        l = 0
        longest= 0
        
        for r in range(len(s)):
#             if letter in set than remove everything before this cur position
            while s[r] in char:
                char.remove(s[l])
                l+=1
            char.add(s[r])
            longest = max(longest, r-l+1)
        return longest
            
                