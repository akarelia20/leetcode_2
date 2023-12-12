class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        # itrate each letter and put them in a dict
        dict_s = {}
        dict_t = {}
        
        for i in range(len(s)):
            if s[i] in dict_s:
                dict_s[s[i]] = dict_s[s[i]]+1
            else: 
                dict_s[s[i]] = 1 
            if t[i] in dict_t:
                dict_t[t[i]] = dict_t[t[i]]+1
            else:
                dict_t[t[i]] = 1
        return dict_s == dict_t
            