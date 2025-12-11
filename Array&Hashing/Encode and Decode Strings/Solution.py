class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = []
        for str in strs:
            encodedStr.append(f"{len(str)}#{str}")
        
        return "".join(encodedStr)

    def decode(self, s: str) -> List[str]:
        index_current = 0
        index_iter = 0
        results = []
        while index_iter < len(s):
            if s[index_iter] == '#':
                char_count = int(s[index_current:index_iter])
                end_location = index_iter+char_count+1
                results.append(s[index_iter+1:end_location])
                index_current = end_location
                index_iter = end_location
            else:
                index_iter+=1
        
        return results
