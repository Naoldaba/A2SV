class Solution:
    def average(self, salary: List[int]) -> float:
        new_sal=sorted(salary)
        sum=0
        for i in range(1, len(salary)-1):
            sum+=new_sal[i]
        return sum/(len(salary)-2)
