class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod=10**9+7
        prefix=[0]*len(nums)
        for st, end in requests:
            prefix[st]+=1
            if end+1<len(nums):
                prefix[end+1]-=1
        for i in range(1,len(prefix)):
            prefix[i]+=prefix[i-1]
        ans = sum(num*count for num, count in zip(sorted(nums), sorted(prefix)))
        return ans%mod
        