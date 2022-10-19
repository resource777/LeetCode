class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        tmp = columnNumber
        res = ""
        s = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        while tmp:
            idx = tmp%26
            res+=s[idx]
            if idx == 0:
                tmp -=26
            else:
                tmp -=idx
            tmp//=26
        return res[::-1]
            