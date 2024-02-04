class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic={0:1}
        prefix=rem=count=0
        for i in range(len(nums)):
            prefix+=nums[i]
            rem=prefix % k
            if rem in dic:
                count+=dic[rem]
            dic[rem]=1+dic.get(rem, 0)
        return count

        