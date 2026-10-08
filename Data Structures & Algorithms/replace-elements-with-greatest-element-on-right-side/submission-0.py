class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        big = -1
        ans = []
        for i in range(len(arr)-1, -1, -1):
            ans.append(big)
            big = max(big, arr[i])
        return ans[::-1]