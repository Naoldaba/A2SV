class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if stack and s[i]=='*':
                stack.pop()
            elif s[i]!='*':
                stack.append(s[i])
        return ''.join(stack)
        