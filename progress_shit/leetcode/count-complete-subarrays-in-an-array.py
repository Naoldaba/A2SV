class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        n = len(set(nums))
        l=0
        ans=0
        for r in range(len(nums)):
            dic[nums[r]]+=1
            while len(dic)==n:
                dic[nums[l]]-=1
                if dic[nums[l]]==0:
                    del dic[nums[l]]
                l+=1
            ans+=l
        return ans
    
            
        
             