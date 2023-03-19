class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # stores indexes
        stack = []
        # result arr
        res= []
        
        for i in range(len(temp)):
            if i== 0:
                res.append(0)
                stack.append(i)
                # print(stack, res)
            else: 
                res.append(0)
                # print(temp[stack[-1]],temp[i] )
                while stack and temp[stack[-1]] < temp[i]:
                    res[stack[-1]]= i-(stack[-1])
                    stack.pop()
            
                stack.append(i)
#                 print(stack, res)
        return res
               
                   
                