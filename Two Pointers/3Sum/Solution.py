class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                # [0 0 0 0 0 0] -> 
                continue
            # leave at least two spaces for j and k
            left, right = i + 1, len(nums)-1
            while left < right:
                # [-6 1 2 4 5]
                sum_cur = nums[i] + nums[left] + nums[right]
                if sum_cur > 0:
                    right -= 1
                elif sum_cur < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]: left+=1
                    while left < right and nums[right] == nums[right+1]: right -=1
            
        return result