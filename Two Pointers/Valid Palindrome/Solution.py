class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = []
        for char in s:
            if char.isalnum():
                clean_str.append(char.lower())
        
        n = len(clean_str)
        for i in range(n//2):
            # [a b c b a]: 0, 1, 2
            # [a b c c b a]: 0, 1, 2
            if clean_str[i] != clean_str[n - i - 1]:
                return False
        return True

# The alternative two-pointer approach
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True