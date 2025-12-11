class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #      [1, 2, 4, 6]
        # left [1, 1, 2, 8]
        # right[48, 24, 6, 1]
        n = len(nums)
        left = [1]*n
        for i in range(1, n):
            left[i] = nums[i-1]*left[i-1]

        right = [1]*n
        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1]*right[i+1]

        result = []
        for i in range(n):
            result.append(left[i]*right[i])

        return result