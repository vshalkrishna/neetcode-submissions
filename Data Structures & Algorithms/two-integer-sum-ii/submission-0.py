class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        q = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in q and diff != nums[i]:
                return [q[diff]+1, i+1]
            q[nums[i]] = i