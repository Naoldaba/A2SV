class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        new_points=sorted(points)
        count=1

        i=1
        cur_end=new_points[i-1][1]

        while i<len(points):
            if new_points[i][0]<=cur_end:
                cur_end=min(cur_end, new_points[i][1])
                i+=1
            else:
                count+=1
                cur_end=new_points[i][1]
                i+=1
            # print(cur_max)

        return count
            

        