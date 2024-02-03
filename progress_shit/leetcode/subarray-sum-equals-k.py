class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict=defaultdict(int)
        sum_dict[0]=1
        prefix=count=0

        for num in nums:
            prefix+=num
            if prefix-k in sum_dict:
                count+=sum_dict[prefix-k]
            sum_dict[prefix]+=1
        return count
        
        