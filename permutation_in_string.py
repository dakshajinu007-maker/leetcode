class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        k=len(s1)
        window={}
        d1={}
        for i in range(k):
            if s1[i] in d1:
                d1[s1[i]]=d1[s1[i]]+1
            else:
                d1[s1[i]]=1
        for i in range(k):
            if s2[i] in window:
                window[s2[i]]=window[s2[i]]+1
            else:
                window[s2[i]]=1
        if d1==window:
            return True
        for i in range(len(s2)-k):
            leaving=s2[i]
            coming=s2[i+k]
            if window[leaving]==1:
                del window[leaving]
            else:
                window[leaving]=window[leaving]-1
            if coming in window:
                window[coming]=window[coming]+1
            else:
                window[coming]=1
            if d1==window:
                return True
        return False