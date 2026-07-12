class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        s=0
        prefix={0:1}
        for  i in nums:
            s+=i
            if s-k in prefix:
                c+=prefix[s-k]
            if s in prefix:
                prefix[s] += 1
            else:
                prefix[s] = 1
        return c