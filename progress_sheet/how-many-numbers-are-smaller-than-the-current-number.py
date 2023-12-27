class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=defaultdict(int)
        arr=[]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    count[nums[i]]+=1
            arr.append(count[nums[i]])
            count.clear()
        return arr


        