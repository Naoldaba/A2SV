class Solution:
    def largestOddNumber(self, num: str) -> str:
        result=""
        rev=num[::-1]
        for i in range(len(rev)):
            if int(rev[i])%2==1:
                result=rev[i:]
                break
        return result[::-1]

            


            


        