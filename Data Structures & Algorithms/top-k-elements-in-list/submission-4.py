class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = 1 + maps.get(nums[i], 0)
        num_sort = sorted(nums, key = lambda x : maps[x], reverse = True)
        nums=num_sort
        seen = set()
        ans = []
        for i in nums:
            if i not in seen:
                seen.add(i)
                ans.append(i)
        return ans[:k]