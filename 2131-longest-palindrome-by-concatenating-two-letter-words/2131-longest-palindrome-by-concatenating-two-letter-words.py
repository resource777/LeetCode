class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = {}
        for w in words:
            if w not in dic:
                dic[w] = 1
            else:
                dic[w] += 1
        print(dic)
        ans=0
        for w in dic:
            if w[1] == w[0]:
                if dic[w] >= 2:
                    ans+=(dic[w]//2*4)
                    dic[w]-=((dic[w]//2)*2)
            elif w[1]+w[0] in dic:
                tmp = min(dic[w[1]+w[0]],dic[w])
                dic[w] -= tmp
                dic[w[1]+w[0]] -= tmp
                ans+=4*tmp
        for w in dic:
            if w[1] == w[0] and dic[w] == 1:
                ans+=2
                break
        return ans
            
                