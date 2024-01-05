class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dic={}
        result=[]
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                Sum=nums[i]+nums[l]+nums[r]
                if Sum==0:
                    ind=[nums[i],nums[l],nums[r]]
                    if str(ind) in dic:
                        dic[str(ind)]+=1
                    else:
                        dic[str(ind)]=1
                        result.append(ind)
                    l+=1
                    r-=1
                elif Sum>0:
                    r-=1
                else:
                    l+=1
        return result