class Solution:
    def reverseWords(self, s: str) -> str:
        new_str=s.strip().split(" ")
        new_str=new_str[::-1]
        print(new_str)
        ans=[]
        for i in range(len(new_str)):
            if new_str[i]:
                ans.append(new_str[i])
        return " ".join(ans)