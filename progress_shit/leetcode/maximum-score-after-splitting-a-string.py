class Solution:
    def maxScore(self, s: str) -> int:
        r_sum=0
        for num in s:
            r_sum+=int(num)
        l_sum=0
        count=0
        ans=0
        for i in range(len(s)-1):
            l_sum+=int(s[i])
            Sum=(i+1-l_sum)+(r_sum-l_sum)
            ans=max(Sum, ans)
        return ans



