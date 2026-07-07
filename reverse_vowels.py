class Solution:
    def reverseVowels(self, s: str) -> str:
        b=0
        e=len(s)-1
        l=list(s)
        while(b<e):
            if l[b]  not in "AEIOUaeiou":
                b+=1
            elif l[e] not in "AEIOUaeiou":
                e-=1
            else:
                temp=l[b]
                l[b]=l[e]
                l[e]=temp
                b+=1
                e-=1
        return "".join(l)