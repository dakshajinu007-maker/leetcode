class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        l=len(p)
        w={}
        a={}
        index=[]
        for i in range(l):
            if p[i] in a:
                a[p[i]]=a[p[i]]+1
            else:
                a[p[i]]=1
        for i in range(l):
            if s[i] in w:
                w[s[i]]=w[s[i]]+1
            else:
                w[s[i]]=1
        if w==a:
            index.append(0)
        for i in range(len(s)-l+1):
            if i == len(s) - l:
                break
            first=s[i]
            last=s[i+l]
            if first in w:
                if w[first]>1:
                    w[first]=w[first]-1
                else:
                    del w[first]
            if last in w:
                w[last]=w[last]+1
            else:
                w[last]=1
            if w==a:
                index.append(i+1)
        return index