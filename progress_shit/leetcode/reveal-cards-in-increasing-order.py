class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        ans=deque([deck[0]])

        for i in range(1, len(deck)):
            end=ans.pop()
            ans.appendleft(end)
            ans.appendleft(deck[i])
        return list(ans)