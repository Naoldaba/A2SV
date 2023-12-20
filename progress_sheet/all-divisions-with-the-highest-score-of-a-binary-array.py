class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dic=defaultdict(int)
        left=0
        right=sum(nums)
        i=0
        dic[0]=left+right
        dic[len(nums)]=len(nums)-right
        ans=[]

        while i<len(nums):
            if nums[i]==0:
                left+=1
            elif nums[i]==1:
                right-=1
            dic[i+1]=left+right
            i+=1
        Max=max(dic.values())
        for i in dic.keys():
            if dic[i]==Max:
                ans.append(i)
        return ans

            

        