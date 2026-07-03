class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        d2={}
        for i in range(len(s)):
            if (s[i] in d and d[s[i]]!=t[i]) or (t[i] in d2 and d2[t[i]]!=s[i]):
                return False
            else:
                d2[t[i]]=s[i]
                d[s[i]]=t[i]
        return True