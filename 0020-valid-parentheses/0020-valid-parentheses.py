class Solution:
    def isValid(self, s: str) -> bool:
        set = {'{':'}', '[':']', '(':')'}
        stack = []
        for i in s:
            if stack:
                x = stack[-1]
                if x in set and i == set[x]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
            
            
        if stack == []:
            return True
        
        return False
            
            