class Solution:
    def minimumSteps(self, s: str) -> int:

        j = 0
        res = 0
        for i in range(len(s)):
            if s[i] == '0':
                res += i - j
                j += 1
        
        return res