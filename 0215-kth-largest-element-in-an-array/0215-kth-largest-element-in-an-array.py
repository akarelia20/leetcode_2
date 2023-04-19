class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        
        res = 0
        for i in range(k):
            res= heapq.heappop(nums)
            if i+1 == k:
                
                if res < 1:
                    return abs(res)
                else:
                    return -1*(res)
            
        
        
                
                
            
            