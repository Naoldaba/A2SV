class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        Rem=sum(nums)%p
        if Rem == 0:
            return 0
        ans=len(nums)
        dic={0:-1}
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            need=prefix % p
            if (need-Rem)%p in dic:
                ans=min(ans, i-dic[(need-Rem)%p])
            dic[prefix%p]=i
        return ans if ans!=len(nums) else -1

        