class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        Min=float('inf')
        Diff=float('inf')
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                Sum=nums[i]+nums[l]+nums[r]
                if target-Sum==0:
                    return Sum
                elif Sum>target:
                    r-=1
                else:
                    l+=1
                if abs(Sum-target)<Diff:
                    Min=Sum
                    Diff=abs(Sum-target)
        return Min
                
        