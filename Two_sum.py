class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen={}
      l=len(nums)
      for i in range(l):
        compliment=target-nums[i]
        if compliment in seen:
            return [seen[compliment],i]
        seen[nums[i]]=i