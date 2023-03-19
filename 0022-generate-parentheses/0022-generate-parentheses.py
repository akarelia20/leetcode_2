class Solution:
    def generateParenthesis(self, n: int) -> List[str]: 
        result = []
        s = ""
        z= ""
        
    
        def helper(openN, closeN, s):
            if openN == closeN == n:
                result.append(s)
                return
            if openN < n:
                print("s",s+"(")
                z = s+"("
                print(s )
                helper(openN+1, closeN, z)
                
            if closeN < openN:
                s += ")"
                helper(openN, closeN + 1, s)
                # s= ""
        
        helper(0 , 0, s)
        return result
    
    #         open, close = n
#         add close parenthesis only when close is less than open (close < open)
#         each sting of combination always starts with open parenthesis
        