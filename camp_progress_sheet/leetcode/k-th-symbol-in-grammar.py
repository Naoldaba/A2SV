class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        curr=0
        l, r= 1, 2**(n-1)
        
        for _ in range(n-1):
            mid=(l+r)//2
            # print(mid)
            
            if k<=mid:
                r=mid
            else:
                l=mid+1
                curr=0 if curr==1 else 1
        return curr