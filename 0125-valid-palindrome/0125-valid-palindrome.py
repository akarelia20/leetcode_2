class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= "".join(e for e in s if e.isalnum()).lower()
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
            
        
        