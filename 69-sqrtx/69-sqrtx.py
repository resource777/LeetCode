class Solution:
    def mySqrt(self, x: int) -> int:
        s = 1
        while s*s <=x:
            if s*s == x:
                return s
            s+=1
        return s-1