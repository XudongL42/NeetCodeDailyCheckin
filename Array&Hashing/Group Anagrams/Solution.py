from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = set()
        str_counters = {}
        results = []
        for word in strs:
            str_counters[word] = Counter(word)
        
        for i in range(len(strs)):
            word = strs[i]
            if i not in visited:
                holder = [word]
                visited.add(i)
                for j in range(i+1, len(strs)):
                    if j not in visited and str_counters[word] == str_counters[strs[j]]:
                        holder.append(strs[j])
                        visited.add(j)
                results.append(holder)

        return results
    
# An optimized version using sorted strings as keys suggested by AI
from collections import Counter, defaultdict
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_counters = defaultdict(list)

        for word in strs:
            char_count = [0]*26
            for char in word:
                char_index = ord(char) - ord('a')
                char_count[char_index]+=1
            word_key = tuple(char_count)
            str_counters[word_key].append(word)
        
        return list(str_counters.values())
