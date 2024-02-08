class Solution:
    def numberOfWays(self, s: str) -> int:
        total_ones=s.count('1')
        total_zeros=len(s)-total_ones
        ans=zero_prefix=one_prefix=0
        for char in s:
            if char == '0':
               ans+=one_prefix*(total_ones-one_prefix)
               zero_prefix+=1
            else:
                ans+=zero_prefix*(total_zeros-zero_prefix)
                one_prefix+=1
        return ans

# [0,0,1,1,0,1]

# [0,0,1,2,2,3]
        