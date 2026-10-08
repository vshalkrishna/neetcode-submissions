class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        while low < high:
            ans = nums[low] + nums[high]
            if nums[low] != nums[high] and ans == target:
                return [low+1, high +1]
            elif ans < target:
                low += 1
            else:
                high -= 1