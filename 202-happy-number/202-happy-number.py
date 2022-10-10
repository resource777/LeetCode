class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            s.add(n)
            n = str(n)
            sum=0
            for digit in n:
                sum+=int(digit)**2
            
            if sum == 1:
                return True
            else:
                n=sum
            if sum in s:
                break
        return False
            
                