class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_len=len(firstList)
        last_len=len(secondList)
        i=0
        j=0
        ans=[]
        while i<first_len and j<last_len:
            if firstList[i][0]>secondList[j][1]:
                j+=1
            elif secondList[j][0] > firstList[i][1]:
                i+=1
            else:
                ans.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                if firstList[i][1]>secondList[j][1]:
                    j+=1
                elif secondList[j][1]>firstList[i][1]:
                    i+=1
                else:
                    i+=1
                    j+=1
        return ans
                