class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=s.split()
        if len(pattern)!=len(l):
            return False
        d={}
        d2={}
        for i in range(len(pattern)):
            if (pattern[i] in d and d[pattern[i]]!=l[i])or (l[i] in d2 and d2[l[i]]!=pattern[i] ):
                return False
            else:
                d2[l[i]]=pattern[i]
                d[pattern[i]]=l[i]
        return True