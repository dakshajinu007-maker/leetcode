class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        candidate=None
        for num in nums:
            if c==0:
                candidate=num
            if candidate==num:
                c+=1
            else:
                c-=1
        return candidate