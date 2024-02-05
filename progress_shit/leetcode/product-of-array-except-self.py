class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        postfix=[1]
        for i in range(len(nums)):
            prefix.append(prefix[-1]*nums[i])
        for i in range(len(nums)-1,-1,-1):
            num=nums[i]*postfix[0]
            postfix=[num]+postfix
        print(postfix)
        ans=[]
        for i in range(len(nums)):
            ans.append(prefix[i]*postfix[i+1])
        return ans