class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        
        print(nums)
        res = 0
        for i in range(k):
            if i+1 == k:
                res = heapq.heappop(nums)
                if res < 1:
                    return abs(res)
                else:
                    return -1*(res)
            heapq.heappop(nums)
        
        
                
                
            
            