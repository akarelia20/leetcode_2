class Solution:
    def generateParenthesis(self, n: int) -> List[str]: 
#         open, close = n
#         add close parenthesis only when close is less than open (close < open)
#         each sting of combination always starts with open parenthesis
     
        result = []
        s = ""
        z= ""
        
    
        def helper(openN, closeN, s):
            if openN == closeN == n:
                result.append(s)
                return
            if openN < n:
                helper(openN+1, closeN, s+"(")
                
            if closeN < openN:
                helper(openN, closeN + 1, s +")")
              
        
        helper(0 , 0, s)
        return result
    
     