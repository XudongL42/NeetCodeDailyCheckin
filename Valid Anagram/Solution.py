class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count_s = {}
        char_count_t = {}

        for char_s in s:
            char_count_s[char_s] = char_count_s.get(char_s, 0) + 1

        for char_t in t:
            char_count_t[char_t] = char_count_t.get(char_t, 0) + 1

        for (key_s, value_s) in char_count_s.items():
            if key_s not in char_count_t or char_count_t[key_s] != value_s:
                return False
        
        return True

# An optimized version using collections.Counter suggested by AI 
from collections import Counter
class Solutions:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same length
        if len(s) != len(t):
            return False
        
        # Two strings are anagrams if and only if they have the 
        # exact same character counts, which means their Counters are equal.
        return Counter(s) == Counter(t)