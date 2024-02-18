class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        absolute_path=path.split('/')
        for i in absolute_path:
            if stack and i=='..':
                stack.pop()
            elif i not in ['','.','..']:
                stack.append(i)
        return '/'+'/'.join(stack)
        

        