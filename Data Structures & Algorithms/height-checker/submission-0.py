class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered = sorted(heights)
        count= 0
        for i in range(len(heights)):
            if ordered[i] != heights[i]:
                count += 1
        return count