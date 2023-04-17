class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            first_max = abs(heapq.heappop(maxHeap))
            second_max = abs(heapq.heappop(maxHeap))
            
            if first_max > second_max:
                heapq.heappush(maxHeap, -1*(first_max-second_max))
            
                
        return abs(maxHeap[0]) if maxHeap else 0