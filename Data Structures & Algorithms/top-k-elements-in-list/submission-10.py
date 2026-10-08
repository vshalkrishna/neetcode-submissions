class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums = [1, 1, 2, 2, 3, 3, 3, 4] ' 1->4, 2 ->[2,3],3->4
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        #now count will have 1->2,2->2,3->3,4->1 , 1->[4],2->[2,1],3->[3]
        occur = [[] for i in range(len(nums)+1)]
        for key, value in count.items():
            occur[value].append(key)
        
        res = []
        for i in range(len(occur)-1, -1, -1):
            #at one cell there can be n values lets take [1, 1, 1, 1,1] = at 5th index 1 will be there
            for x in occur[i]:
                res.append(x)
                if len(res) == k:
                    return res