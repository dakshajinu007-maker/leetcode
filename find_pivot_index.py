class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        lsum=0
        for i in range(len(nums)):
            current=nums[i]
            if total==(2*lsum)+current:
                return i
            lsum+=current
        return -1
