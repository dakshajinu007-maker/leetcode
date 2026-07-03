class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def square_value(self,n):
            s=0
            while(n>0):
                s+=(n%10)*(n%10)
                n//=10
            return s
        x=n
        while (x!=1):
            if x in seen:
                return False
            seen.add(x)
            x=square_value(self,x)
        return True
        



            