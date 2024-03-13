class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def withinDays(cap):
            curdays=1
            currweight=cap
            for w in weights:
                if currweight - w < 0:
                    curdays+=1
                    currweight=cap
                currweight-=w
            return curdays<=days

        left, right = max(weights), sum(weights)
        ans=sum(weights)

        while left<=right:
            mid=(left+right)//2
            if withinDays(mid):
                ans=min(ans, mid)
                right=mid-1
            else:
                left=mid+1
        return ans

        
        


        