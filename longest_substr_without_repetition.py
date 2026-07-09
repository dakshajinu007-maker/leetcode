class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        window={}
        max_len=0
        for right in range (len(s)):
            char=s[right]
            if char in window and window[char]>=left:
               left=window[char]+1
            window[char]=right
            l=right-left+1
            if l>max_len:
                max_len=l
        return max_len