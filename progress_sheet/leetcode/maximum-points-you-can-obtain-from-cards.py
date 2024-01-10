class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        total= sum(cardPoints)
        remaining_length=n-k
        sub_array=sum(cardPoints[:remaining_length])
        min_sum=sub_array
        for j in range(remaining_length, n):
            sub_array+=cardPoints[j]
            sub_array-=cardPoints[j-remaining_length]
            min_sum=min(min_sum, sub_array)
        return total-min_sum

            
            


        