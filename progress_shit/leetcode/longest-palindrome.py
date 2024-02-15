class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic=Counter(s)
        values=list(dic.values())
        print(values)
        Max=0
        flag=0
        for i in range(len(values)):
            if values[i]%2==0:
                Max+=values[i]
            else:
                flag=1
                Max+=values[i]-1

        if flag:
            return Max+1
        return Max

        