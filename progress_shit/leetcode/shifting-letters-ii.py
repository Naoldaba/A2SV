class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_arr=[0]*len(s)
        for st, end, di in shifts:
            if di==1:
                prefix_arr[st]+=1
                if end+1<len(s):
                    prefix_arr[end+1]-=1
            elif di==0:
                prefix_arr[st]-=1
                if end+1<len(s):
                    prefix_arr[end+1]+=1

        for i in range(1,len(prefix_arr)):
            prefix_arr[i]+=prefix_arr[i-1]

        new_str=""
        for i in range(len(prefix_arr)):
            char_rep=(ord(s[i])-ord('a'))
            new_str+=chr(((char_rep+(prefix_arr[i])) % 26)+ord('a'))
        
        print(prefix_arr)
        return new_str
        