class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right and nums[right] < nums[left]:
            mid = (left + right)//2
            print(f"{mid}, {left}, {right}")
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]