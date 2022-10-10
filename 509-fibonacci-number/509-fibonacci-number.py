class Solution:
    def fib(self, n: int) -> int:
        n0=0
        n1=1
        for i in range(2,n+1):
            n0,n1 = n1,n0+n1
        if n ==0:
            return n0
        return n1
            