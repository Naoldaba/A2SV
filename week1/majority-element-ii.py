class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic=defaultdict(int)
        result=set(filter(lambda x: nums.count(x)>floor(len(nums)/3), nums))
        return list(result)
        # for i in range(len(nums)):
        #     if not dic[nums[i]]:
        #         dic[nums[i]]=nums.count(nums[i])
            