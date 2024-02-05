class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans=0
        count=0
        odd=0
        l=0
        for r in range(len(nums)):
            if nums[r]%2==1:
                odd+=1
                count=0
            while odd==k:
                if nums[l]%2==1:
                    odd-=1
                count+=1
                l+=1
            ans+=count
        return ans
            