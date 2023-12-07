class Solution(object):
    def rotate(self,nums, k):
        n = len(nums)
        k = k % n  # Handle cases where k is larger than the array size

        # Reverse the entire array
        self.reverse(nums, 0, n - 1)

        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # Reverse the remaining elements
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         start_pos = len(nums) - k
#         x = []
#         counter = 0
#         if k < len(nums):
#             y = nums[start_pos -1] 
#             for i in range(0,len(nums)):
#                 print(i)
#                 # if ((start_pos+i) < len(nums)):
#                 z = nums[i] 
#                 nums[i] = nums[(start_pos)+i]
#                 nums[(start_pos)+(i-1)] = z
#                 if (i == k-1) and (k!= start_pos):
#                     nums[len(nums)-1] = y
#                 print(x, nums)
        
        
    