class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result=[]
        Min=float('inf')
        set1=set(list1)
        set2=set(list2)
        com=set1.intersection(set2)
        for common in (list(com)):
            Min=min(Min, list1.index(common)+list2.index(common))

        for common in (list(com)):
            if list1.index(common)+list2.index(common)==Min:
                result.append(common)
        return result

            

        