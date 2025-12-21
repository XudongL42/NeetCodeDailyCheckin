class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        p = 0

        s1_chars = {}
        for char in s1:
            s1_chars[char] = s1_chars.get(char, 0) + 1
        
        s2sub_chars = {}
        for char in s2[0:n1]:
            s2sub_chars[char] = s2sub_chars.get(char, 0) + 1
        
        if s1_chars == s2sub_chars:
            return True

        for i in range(n1, n2):
            char_to_add = s2[i]
            char_to_remove = s2[i - n1]
            s2sub_chars[char_to_add] = s2sub_chars.get(char_to_add, 0) + 1
            s2sub_chars[char_to_remove] -= 1

            isPermutation = True
            for key in s1_chars:
                if s1_chars[key] != s2sub_chars.get(key, 0):
                    isPermutation = False
            
            if isPermutation:
                return True
        return False