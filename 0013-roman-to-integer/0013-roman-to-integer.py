class Solution:
    def romanToInt(self, s: str) -> int:
        dict= {"I":1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M": 1000} 
        result = dict[s[len(s)-1]]
        
        
        for i in range(len(s)-2, -1,-1):
            if dict[s[i]] < dict[s[i+1]]:
                result -= dict[s[i]]
            else:
                result += dict[s[i]]
        return result
        