class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so the map is something like count and value
        count = {}
        occurence = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        #arr = [1, 1, 1, 2, 2, 3, 4, 4] = countdictionary = 1 -> 3, 2->2, 3->1, 4->2
        #occurence[i].append(count.value)
        for key, value in count.items():
            occurence[value].append(key) # if 2 and 4 occurece 2 so you should have to append it
        
        res = []
        # run from the end of occurence y? becoz if all the elemnts are 1 
        # [1, 1, 1, 1, 1, 1, ] -> occurence[6].append(1) then that is the max
        for i in range(len(occurence)-1, -1, -1): #occurenct list will be [0,3,[2,4],1]
            for n in occurence[i]:
                res.append(n)
                if len(res) == k:
                    return res