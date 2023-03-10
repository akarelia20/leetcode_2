class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        vol=0
        while l < r:
            x= min(height[l], height [r])
            vol = max(vol, x * (r-l))
            if height[l] < height[r] or height[l] == height [r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
          
        return vol