class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            lsum=nums[0:i]
            rsum=nums[i+1:]
            if sum(lsum)==sum(rsum):
                return i
        return -1