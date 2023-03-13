class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict= {}
        length = 0
        longest = 0
        for i in range(len(s)) :
            if s[i] not in dict:
                length += 1
            else:
                if dict[s[i]] < (len(s)-length):
                    length += 1
                length = min(length, i - dict[s[i]])
            dict[s[i]] = i
            longest = max(longest, length)

        return longest