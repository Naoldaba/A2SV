class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result=[]
        for i in range(len(boxes)):
            count=0
            for j in range(len(boxes)):
                if i!=j and boxes[j]!="0":
                    count+=abs(i-j)
            result.append(count)
        return result


        