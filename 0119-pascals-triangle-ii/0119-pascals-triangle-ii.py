class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[0 for _ in range(34)] for _ in range(34)]
        for i in range(34):
            dp[i][i]=dp[i][0]=1
        for i in range(2, rowIndex+1):
            for j in range(1,i):
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        tmp=[]
        for i in range(rowIndex+1):
            tmp.append(dp[rowIndex][i])
        return tmp
                
        