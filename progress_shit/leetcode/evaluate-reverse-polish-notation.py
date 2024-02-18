class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        Set={'*', "+","-","/"}
        for i in range(len(tokens)):
            if tokens[i] not in Set:
                stack.append(int(tokens[i]))
            else:
                Num2=stack.pop()
                Num1=stack.pop()
                if tokens[i]=='+':
                    stack.append(Num1+Num2)
                elif tokens[i]=='-':
                    stack.append(Num1-Num2)
                elif tokens[i]=='*':
                    stack.append(Num1*Num2)
                else:
                    stack.append(int(Num1/Num2))

        return stack.pop()

        