class Solution:
    def climbStairs(self, n: int) -> int:
#         if n= 1 then possible ways would be possible ways to get to previos step which is n=0 and possible ways would be 0 and way to get to n=1 wpuld be 1 so 1+0 = 1
        prev = 0
        cur = 1
        holder = 0
        for pos_way in range(n):
#             holds value of cur
            holder = cur
#             new current would be prev+cur
            cur = prev+cur
#             new prev would be cur
            prev = holder
        return cur
    
            