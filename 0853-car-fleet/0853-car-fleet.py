import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dict = {}
        stack = []
            
#        postion (key), [speed, steps or iteration to reach target](value)
        for i in range (len(position)):
            dict[position[i]] = [speed[i] ,(target-position[i])/speed[i]]
        position.sort(reverse= True)
     
        
        for j in range(len(position)):
            stack.append(dict[position[j]][1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
                