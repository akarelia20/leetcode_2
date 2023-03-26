import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (r+l)//2
            hr_sum= 0
            for pile in piles:
                hr_sum += math.ceil(pile/mid)
            if hr_sum <= h:
                res = min(res, mid)
                r = mid-1    
            elif hr_sum > h:
                l = mid+1        
        return res
                
           
            
        
    
    
    