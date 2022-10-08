class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        left=right=0
        ans=[]

        def make_parenthese(s, left, right, n):
            if len(s) == 2*n:
                ans.append(s)
                return
            if right>left:
                return
            if left < n :
                make_parenthese(s+'(',left+1,right,n)
            if right < n:    
                make_parenthese(s+')',left,right+1,n)
            

        make_parenthese("", 0, 0, n)
        print(ans)
        return ans
