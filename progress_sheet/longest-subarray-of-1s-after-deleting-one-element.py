class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        Max=j=0
        count_zero=0
        for i in range(len(nums)):
            if nums[i]==0:
                count_zero+=1
            while count_zero>1:
                if nums[j]==0:
                    count_zero-=1
                j+=1
            Max=max(Max, i-j+1)
        return Max-1
            
        