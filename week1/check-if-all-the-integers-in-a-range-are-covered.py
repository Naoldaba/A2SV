class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        new_set=set()
        for ran in range(len(ranges)):
            new_set=new_set.union(list(range(ranges[ran][0], ranges[ran][1]+1)))
        
        for i in range(left, right+1):
            if i not in new_set:
                return False
        return True
        