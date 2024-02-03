class Solution:
    def balancedString(self, s: str) -> int:
        k = len(s)//4
        dic = {'Q':0,'W':0,'E':0,'R':0}
        for char in s:
            dic[char] += 1
        if dic['Q'] == k and dic['W'] == k and dic['E'] == k and dic['R'] == k:
            return 0
        ans = len(s)
        i = 0
        for j in range(len(s)):
            dic[s[j]] -= 1
            while i < len(s) and dic['Q'] <= k and dic['W'] <= k and dic['E'] <= k and dic['R'] <= k:
                ans = min(ans, j-i+1)
                dic[s[i]] += 1
                i += 1
        return ans