class Solution:
    def trap(self, height: List[int]) -> int:
        # Original implementation (precompute left/right max arrays)
        from_left = [0] * len(height)
        left_max = 0
        for i in range(len(height)):
            left_max = left_max if left_max > height[i] else height[i]
            from_left[i] = left_max

        from_right = [0] * len(height)
        right_max = 0
        for i in range(len(height) - 1, -1, -1):
            right_max = max(right_max, height[i])
            from_right[i] = right_max

        result = 0
        for i in range(len(height)):
            result += max(min(from_left[i], from_right[i]) - height[i], 0)
        return result

class Solution2:
    def trap_two_pointer(self, height: List[int]) -> int:
        """
        Optimized two-pointer implementation (O(n) time, O(1) extra space).
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max = right_max = 0
        result = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1

        return result