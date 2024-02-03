class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=[]
        self.prefix_sum=[0]
        for i in range(len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1]+nums[i])
        print(self.prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1]-self.prefix_sum[left]

        
[0,-2,-2,1,-4,-2,-3]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)