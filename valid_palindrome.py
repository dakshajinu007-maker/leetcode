class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in s:
            if i.isalnum():
                t+=i.lower()
        b=0
        e=len(t)-1
        while(b<e):
            if t[b]!=t[e]:
                return False
            b+=1
            e-=1
        return True