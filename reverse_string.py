class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        b=0
        e=len(s)-1
        while(b<e):
            temp=s[b]
            s[b]=s[e]
            s[e]=temp
            b+=1
            e-=1
        