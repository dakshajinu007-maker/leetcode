class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wsum=sum(nums[:k])
        max_sum=wsum
        for i in range(len(nums)-k):
            wsum=wsum-nums[i]+nums[i+k]
            if wsum>max_sum:
                max_sum=wsum
        return max_sum/k