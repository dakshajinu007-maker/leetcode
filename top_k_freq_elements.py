class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map={}
        bucket=[[] for _ in range(len(nums)+1)]
        for i in nums:
            if i in f_map:
                f_map[i]=f_map[i]+1
            else:
                f_map[i]=1
        for num, freq in f_map.items():
            bucket[freq].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res