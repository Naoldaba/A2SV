class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans=[]
        total=sum(nums)
        n=len(nums)
        prefix_sum=0

        for i, num in enumerate(nums):
            prefix_sum+=num
            ans.append(((i+1)*num - prefix_sum) + (total-prefix_sum)-(n-i-1)*num)
            
        return ans

        