class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        
        return False

# Alternative solution proposed by AI
class Solution2:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))