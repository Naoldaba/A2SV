class Solution:
    def largestGoodInteger(self, num: str) -> str:
        long_substring=""
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i]==num[i+2]:
                if num[i]>long_substring:
                    long_substring=num[i]
        return long_substring*3

        