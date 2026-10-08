from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictionary = defaultdict(list)
        
        for i in range(len(s)):
            dictionary[s[i]].append(i)
            
        min_val = float('inf')
        
        for key, val in dictionary.items():
            if len(val) == 1:
                min_val = min(min_val, val[0])
                
        return min_val if min_val != float('inf') else -1