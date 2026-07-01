class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        for i in range (len(nums)) :
            x=nums[i]
            if x in seen:
                if (i-seen[x])<=k:
                    return True
            seen[x]=i
        return False