class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(cards)==1:
            return -1
        dic={cards[0]:0}
        Min=float('inf')
        for r in range(1,len(cards)):
            if cards[r] in dic:
                Min=min(Min, r-dic[cards[r]]+1)
                dic[cards[r]]=r
            else:
                dic[cards[r]]=r
        return Min if Min!=float("inf") else -1

                





        