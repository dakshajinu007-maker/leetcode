class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l=len(accounts)
        large=sum(accounts[0])
        for i in range(l):
            if sum(accounts[i])>large:
                large=sum(accounts[i])
        return large
