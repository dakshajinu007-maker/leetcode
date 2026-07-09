class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow="AEIOUaeiou"
        window=s[:k]
        c=0
        for i in range(len(window)):
            if window[i] in vow:
                c+=1
        max_count=c
        for i in range(len(s)-k):
            if s[i] in vow:
                c-=1
            if s[i+k] in vow:
                c+=1
            if c>max_count:
                max_count=c
        return max_count