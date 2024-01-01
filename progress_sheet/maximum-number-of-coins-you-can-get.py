class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        ans=0
        i=1
        steps=len(piles)//3
        while steps>0:
            ans+=piles[i]
            i+=2
            steps-=1
        return ans
            

        