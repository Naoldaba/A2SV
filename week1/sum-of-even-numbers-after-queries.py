class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # store={i:num for i, num in enumerate(nums)}
        ans=[]
        Sum=sum(list(filter(lambda x: x%2==0, nums)))
        for val, i in queries: 
            temp=nums[i]      
            nums[i]+=val
            if temp%2==0 and nums[i]%2==0:
                Sum+=val
            elif nums[i]%2==0:
                Sum+=nums[i]
            elif temp%2==0 and nums[i]%2==1:
                Sum-=temp
            ans.append(Sum)
        return ans

        