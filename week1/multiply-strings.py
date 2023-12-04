class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic=defaultdict(int)
        for i in range(10):
            dic[str(i)]=i
        li1, li2=[], []
        for i, num in enumerate(num1[::-1]):
            li1.append(dic[num]*(10**i))
        for i, num in enumerate(num2[::-1]):
            li2.append(dic[num]*(10**i))
        return str(sum(li1)*sum(li2))

        