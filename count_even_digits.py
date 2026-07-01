class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for num in nums:
            s=0
            while(num>0):
                num//=10
                s+=1
            if s%2==0:
                c+=1
        return c
        