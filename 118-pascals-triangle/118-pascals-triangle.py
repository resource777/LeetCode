class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tmp = [[0] * 31 for _ in range(31)]
        for i in range(1,31):
            tmp[i][1] = 1
            tmp[i][i] = 1
        for i in range(3,31):
            for j in range(2,i+1):
                tmp[i][j] = tmp[i-1][j]+tmp[i-1][j-1]
        #print(tmp)
        ans = []
        for i in range(1,numRows+1):
            bin = []
            for j in range(1,i+1):
                bin.append(tmp[i][j])
            ans.append(bin)
        return ans