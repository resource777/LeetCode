class Solution:
    def myPow(self, x: float, n: int) -> float:
        k=0
        tmp = x
        ans=1
        
        if n<0:
            tmp = 1.0/x
            n=-n
            
        while 2**k<=n:
            if (n & (1<<k))!=0:
                ans*=tmp
            tmp = tmp*tmp
            k+=1
        return ans