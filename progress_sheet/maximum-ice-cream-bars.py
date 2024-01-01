class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans=count=0
        for i in range(len(costs)):
            if ans+costs[i]<=coins:
                ans+=costs[i]
                count+=1
        return count
        