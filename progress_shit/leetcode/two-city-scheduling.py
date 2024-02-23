class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        new_costs=sorted(costs, key=lambda x: x[0]-x[1])

        Min_cost=0

        for i in range(len(costs)//2):
            Min_cost+=new_costs[i][0]
        for i in range(len(costs)//2, len(costs)):
            Min_cost+=new_costs[i][1]

        return Min_cost        