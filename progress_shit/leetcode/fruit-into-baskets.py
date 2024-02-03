class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count=defaultdict(int)
        l=result=sum=0

        for r in range(len(fruits)):
            count[fruits[r]]+=1
            sum+=1

            while len(count)>2:
                count[fruits[l]]-=1
                sum-=1
                
                if not count[fruits[l]]:
                    count.pop(fruits[l])
                l+=1
            result=max(result, sum)

        return result



        