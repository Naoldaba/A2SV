class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        Len=len(weights)
        adjecent_sum=[]
        for i in range(Len-1):
            adjecent_sum.append(weights[i]+weights[i+1])
        
        adjecent_sum.sort()

        Max=Min=weights[0]+weights[-1]
        for i in range(k-1):
            Min+=adjecent_sum[i]
            Max+=adjecent_sum[Len-2-i]

        return Max-Min

