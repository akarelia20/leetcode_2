class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         create set which will contain unique val
        unique = set()
# loop through list and add vals to "unique" set and if the value already exsist return true
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False