class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(len(nums)):
            diff = target - nums[i] #ill get the diff
            if diff in maps:
                return [maps[diff], i]
            maps[nums[i]] = i