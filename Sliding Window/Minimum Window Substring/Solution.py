class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen, tlen = len(s), len(t)

        if slen < tlen or tlen <= 0:
            return ""
        
        # build t counter map
        t_ct = {}
        for char in t:
            t_ct[char] = t_ct.get(char, 0) + 1
        
        left, right = 0, 0
        s_ct = {}
        s_ct[s[left]] = 1
        result = ""
        while right < slen:
            if self.dictContains(s_ct, t_ct):
                if len(result) > (right - left + 1) or len(result) == 0:
                    result = s[left:(right + 1)]
                if len(result) == 1:
                    return result
                s_ct[s[left]] -= 1
                left += 1
            else:
                # not contains all chars in t
                right += 1
                if right < slen:
                    s_ct[s[right]] = s_ct.get(s[right], 0) + 1
            print(f"{left}, {right}, {result}, {s_ct}")
        
        return result
                

    
    def dictContains(self, cts: dict, ctt:dict) -> bool:
        # cts contains ctt
        for key in ctt:
            if ctt[key] > cts.get(key, 0):
                return False
        return True