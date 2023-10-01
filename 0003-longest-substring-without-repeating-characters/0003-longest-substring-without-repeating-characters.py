class Solution(object):
    def lengthOfLongestSubstring(self, s):
        output= 0
        i = 0
        pos = {}
        for j in range(len(s)):
             # if already there you check wheather i == value of s[j] meaning pos of i and previous position of repeating letter is same in that case new value of i = i+1(move one char over)
            if s[j] in pos:
                if i == pos[s[j]]:
                    i += 1
                 # move i to the previously recoreded position for the letter
                else:
                    i = max(pos[s[j]]+1, i)
            pos[s[j]] = j
            output = max(output, (j-i)+1)
            
        return output
                