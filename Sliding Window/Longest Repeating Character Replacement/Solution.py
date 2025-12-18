class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left, right = 0, 0
        char_count = {}

        while right < len(s):
            current = s[right]
            char_count[current] = char_count.get(current, 0) + 1
            max_char_count = 0
            for char in char_count:
                max_char_count = max(max_char_count, char_count[char])

            cur_len = right - left + 1

            print(f"{cur_len}, {char_count}, {left}, {right}")
            if (cur_len - max_char_count) <= k:
                max_len = max(max_len, cur_len)
                right += 1
            else:
                char_count[s[left]] = char_count.get(s[left]) - 1
                char_count[s[right]] = char_count.get(s[right]) - 1
                left += 1
        return max_len