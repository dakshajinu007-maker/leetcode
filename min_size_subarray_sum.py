class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum=0
        lp=0
        minl=len(nums)+1
        for i in range(len(nums)):
            current_sum+=nums[i]
            while (current_sum>=target):
                winl=i-lp+1
                if winl<minl:
                    minl=winl
                current_sum-=nums[lp]
                lp+=1
        if minl<=len(nums):
            return minl
        else:
            return 0
