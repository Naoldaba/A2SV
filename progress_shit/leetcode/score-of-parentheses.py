class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        Sum=0
        for c in s:
            if c=='(':
                stack.append(0)
            else:
                val=max(stack.pop()*2, 1)
                stack[-1]+=val
        return stack[-1]
        