class Solution:
    def trap(self, height: List[int]) -> int:
        mon_stack=[]
        ans=0
        for i in range(len(height)):
            while mon_stack and height[mon_stack[-1]]<height[i]:
                temp=mon_stack.pop()

                if not mon_stack:
                    break

                w=i-mon_stack[-1]-1
                h=min(height[i], height[mon_stack[-1]])
                

                ans+=(w*h) - (w*height[temp])
                
            mon_stack.append(i)
        return ans


        