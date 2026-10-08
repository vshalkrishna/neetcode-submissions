class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = 1 + maps.get(nums[i], 0)
        num_sort = sorted(maps.keys(),key = lambda x : maps[x], reverse = True)
        return num_sort[:k]
        