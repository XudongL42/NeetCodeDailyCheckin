class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        half = (m + n) // 2
        # [1, 2, 3, 4, 5] [1, 2, 3, 4]
        if m == 0:
            return (nums2[(n-1)//2] + nums2[n//2]) / 2
        if n == 0:
            return (nums1[(m-1)//2] + nums1[m//2]) / 2

        l1, r1 = 0, m - 1
        while True:
            # use the first list to do binary search
            i = (l1 + r1) // 2
            j = half - i - 2

            pleft1 = nums1[i] if i >=0 else float("-infinity")
            pright1 = nums1[i+1] if (i+1) < m else float("infinity")
            pleft2 = nums2[j] if j >=0 else float("-infinity")
            pright2 = nums2[j+1] if (j+1) < n else float("infinity")
            print(f"{pleft1}, {pright1}, {pleft2}, {pright2}")
            if pleft1 <= pright2 and pleft2 <= pright1:
                if (m + n)%2 == 0:
                    return (min(pright1, pright2) + max(pleft1, pleft2)) / 2
                return min(pright1, pright2)

            elif pleft1 > pright2:
                r1 = i - 1
            else:
                l1 = i + 1

