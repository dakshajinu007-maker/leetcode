class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        pos=len(nums)-1
        result=[0]*len(nums)
        while(l<=r):
            ls=nums[l]*nums[l]
            rs=nums[r]*nums[r]
            if ls>rs:
                result[pos]=ls
                l+=1
            else:
                result[pos]=rs
                r-=1
            pos-=1
        return result