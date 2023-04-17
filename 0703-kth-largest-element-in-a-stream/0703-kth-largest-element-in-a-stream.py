class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # using minHeap data structure to get to largest kth element
        self.minHeap = nums
        self.k = k
        # converts arr to heap data stucture
        heapq.heapify(self.minHeap) 
        # if minHeap contains more than k elements then remove 
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
         # min heap data structure automatically remove the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)  
        return self.minHeap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)