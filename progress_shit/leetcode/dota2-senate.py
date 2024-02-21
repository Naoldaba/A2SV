class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        Rads=deque([i for i in range(len(senate)) if senate[i]=="R"])
        Dirs=deque([i for i in range(len(senate)) if senate[i]=="D"])

        while Rads and Dirs:
            r=Rads.popleft()
            d=Dirs.popleft()

            if r < d:
                Rads.append(len(senate)+r)
            else:
                Dirs.append(len(senate)+d)
        print(Rads, Dirs)

        return "Radiant" if Rads else "Dire"
        