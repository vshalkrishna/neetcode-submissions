class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # nums=[1,4,3,3,2]

        maxCount = 0
        if len(nums) == 1:
            return 1
        count = 1
        for i in  range(1, len(nums)):
            if nums[i-1] < nums[i]:#still increasing
                count += 1
            else:
                count = 1
            maxCount = max(maxCount,count)

        


        count = 1
        for i in  range(1, len(nums)):
            if nums[i-1] > nums[i]:#still increasing
                count += 1
            else:
                count =1
            maxCount = max(maxCount,count)

        return maxCount