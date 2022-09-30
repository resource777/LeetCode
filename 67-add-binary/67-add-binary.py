class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        minlen = min(len(a),len(b))
        maxlen = max(len(a),len(b))
        i=0
        add=0
        ans=''
        while i < minlen:
            ans += str((int(a[i])+int(b[i])+add)%2)
            add = (int(a[i])+int(b[i])+add)//2
            i+=1
        if maxlen ==len(a):
            while i<maxlen:
                ans += str((int(a[i])+add)%2)
                add = (int(a[i])+add)//2
                i+=1
        if maxlen ==len(b):
            while i<maxlen:
                ans += str((int(b[i])+add)%2)
                add = (int(b[i])+add)//2
                i+=1
        if add:
            ans+='1'
        return ans[::-1]
            