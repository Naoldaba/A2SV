class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        Max=j=0
        count_zeros=0
        for i in range(len(nums)):
            if nums[i]==0:
                count_zeros+=1
            while count_zeros>k:
                if nums[j]==0:
                    count_zeros-=1
                j+=1
            Max=max(Max, i-j+1)
        return Max

        