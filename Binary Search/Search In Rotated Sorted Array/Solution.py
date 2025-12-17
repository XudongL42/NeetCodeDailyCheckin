class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                # left to mid is increasing
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    return mid
                else:
                    left = mid + 1
            else:
                # mid to right is increasing
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                elif nums[mid] == target:
                    return mid
                else:
                    right = mid - 1
        
        return -1