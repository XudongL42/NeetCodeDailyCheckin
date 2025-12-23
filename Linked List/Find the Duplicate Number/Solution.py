class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            val = nums[i]
            mval = nums[abs(val) - 1]
            print(f"{i} : {val}, {mval}")
            if mval < 0:
                return abs(val)
            else:
                nums[abs(val)-1] *= -1
        return -1
    

# Unless you know Floyd's Tortoise and Hare algorithm, you may find it hard to come up with the below solution.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        initial = True
        while slow != fast or initial:
            slow = nums[slow]
            fast = nums[nums[fast]]
            initial = False
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow