class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        lookup=defaultdict(list)
        ans=[0]*len(nums)
        for i in range(len(nums)):
            lookup[nums[i]].append(i)
        
        for key, value in lookup.items():
            prefix_sum=0
            suffix_sum=sum(value)
            p_count=0
            s_count=len(value)
            for ind in value:
                suffix_sum-=ind
                s_count-=1
                ans[ind] = ind*p_count - prefix_sum + suffix_sum - ind*s_count
                p_count+=1
                prefix_sum+=ind

        return ans