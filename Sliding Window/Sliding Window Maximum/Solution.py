class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # populdate the deque with first window
        window = []
        for i in range(k):
            heapq.heappush(window, (-nums[i], i))
        
        result = [-window[0][0]]
        start = k
        while start < len(nums):
            heapq.heappush(window, (-nums[start], start))
            window_max = window[0]
            print(f"{start}, {window_max}")
            while window_max[1] < start - k + 1:
                heapq.heappop(window)
                window_max = window[0]
                print(f"{start}, {window_max}, inner")
            result.append(-window_max[0])
            start += 1
        return result


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        result = []
        for i in range(len(nums)):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i >= (k - 1):
                while dq[0] <= (i - k):
                    dq.popleft()
                result.append(nums[dq[0]])
            print(f"{i}, {dq}")
        return result