class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic=Counter(answers)


        res=0
        for asked, freq in dic.items():
            res+=math.ceil(freq/(asked+1))*(asked+1)
        return res

        