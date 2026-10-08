class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            marking = [0] * 26
            for c in s:
                marking[ord(c)- 97] += 1
            key = tuple(marking)
            if key not in seen:
                seen[key] = [s] #its a list
            else:
                seen[key].append(s)  # seen[key] has a value list
        return seen.values()