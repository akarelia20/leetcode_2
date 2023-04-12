class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
# using the numbers of an array as an pointer
# example = [1,3,4,2,2] meaning 1 points at post1(val3), 3 points at pos3(val2), 4 points at pos4(val2), 2 points at pos2(4) and 2 points at pos2(4). 
# which creates cyclis list so solving this problem in a similer way as cyclic linked list with fast and slow pointers
        slow, fast, slow2 = 0, 0, 0
        
#condition just to start the loop , loop never go into infinite,there is always an answer 
        while True:     
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow, fast)
            if slow == fast:
                while slow2 != fast:
                    slow2= nums[slow2] #starts from beginning at speed 1
                    fast= nums[fast] #speed 1
                    if slow2 == fast:
                        return slow2 
                    
# floyd's tortoise and hare problem using linked list
        
