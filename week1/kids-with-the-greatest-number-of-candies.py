class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Max=max(candies)
        result=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies<Max:
                result.append(False)
            else:
                result.append(True)
        return result
        