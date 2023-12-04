class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count=1
        forward=0
        cap=capacity
        while forward<len(plants)-1:
            if cap>=plants[forward]:
                cap-=plants[forward]
            if cap>=plants[forward+1]:
                forward+=1
                count+=1
            else:
                cap=capacity
                count+=(2*(forward+1)+1)
                forward+=1
        return count