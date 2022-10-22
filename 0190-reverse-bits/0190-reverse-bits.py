class Solution:
    def reverseBits(self, n: int) -> int:
        tmp =""
        num=n
        while num:
            if num%2==0:
                tmp+='0'
            else:
                tmp+='1'
            num=num//2
        for i in range(32-len(tmp)):
            tmp+='0'
        ans=0
        power = 2**31
        for i in range(32):
            ans+=power*int(tmp[i])
            power//=2
        
        return ans