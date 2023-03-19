class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # stack stores indexes and res stores the #of days
        stack = []
        res= []
        
        for i in range(len(temp)):
            # first index append index into stack and append 0 in res
            if i== 0:
                res.append(0)
                stack.append(i)
             
            # if not first index append 0 in "res" array
            else: 
                res.append(0)
                while stack and temp[stack[-1]] < temp[i]: #until temp[i] > the last stack-val
                    res[stack[-1]]= i-(stack[-1])   
                    stack.pop()    #pop the last index from stack
                stack.append(i)    # append cur index in stack

        return res
               
                   
                