class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        
        left, right = 0, 1
        max_len = 1
        visited = {s[0]:0}
        
        while right < n:
            if s[right] not in visited or visited[s[right]] < left:
                max_len = max(max_len, right - left + 1)
            else:
                # [xyzhyx]
                left = min(visited.get(s[right]) + 1, right)
            visited[s[right]] = right
            right += 1
        
        return max_len