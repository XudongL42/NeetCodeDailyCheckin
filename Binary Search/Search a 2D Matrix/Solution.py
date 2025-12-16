class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        up, bottom = 0, m - 1
        while up <= bottom:
            mid = up + (bottom - up)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                if up == mid: break
                up = mid
        m_index = up if matrix[bottom][0] > target else bottom

        n = len(matrix[0])
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left)//2
            if matrix[m_index][mid] == target:
                return True
            elif matrix[m_index][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

# ============================================================================
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and matrix[i][j] < target:
            i += 1
        if i == m:
            return False

        while j >= 0 and matrix[i][j] >= target:
            if matrix[i][j] == target:
                return True
            j -= 1
        return False