class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequency = {}
        result = []
        for num in nums:
            num_frequency[num] = num_frequency.get(num, 0)+1

        sorted_frequency = sorted(num_frequency.items(), key=lambda x:x[1], reverse=True)

        if k > len(sorted_frequency):
            raise Exception("k must be smaller than")

        for i in range(k):
            result.append(sorted_frequency[i][0])

        return result
    
# Time Complexity: O(N log N) where N is the number of unique elements in nums
# Space Complexity: O(N) where N is the number of unique elements in nums

# Optimized Approach using Bucket Sort
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        sorted_bucket = [[] for l in range(len(nums))]
        for key, value in freq_map.items():
            sorted_bucket[value-1].append(key)
        
        flatend_list = []
        for sublist in reversed(sorted_bucket):
            flatend_list.extend(sublist)
        
        return flatend_list[:k]

# Solution suggested by AI   
from typing import List

# Optimized Approach using Bucket Sort
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Create buckets where index represents frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # Collect k most frequent elements from highest frequency buckets
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]
        
        return result