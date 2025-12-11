class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        deduped = set(nums)
        longest = 0
        for num in nums:
            if num in visited:
                continue
            left = self.toLeft(num, deduped, visited)
            right = self.toRight(num, deduped, visited)
            total = left + right + 1
            longest = longest if longest >= total else total
        return longest

    def toLeft(self, num: int, deduped: Set[int], visited: Set[int]) -> int:
        left = num - 1
        while left in deduped:
            visited.add(left)
            left -= 1
        return num - left - 1 

    def toRight(self, num: int, deduped: Set[int], visited: Set[int]) -> int:
        right = num + 1
        while right in deduped:
            visited.add(right)
            right += 1
        return right - 1 - num