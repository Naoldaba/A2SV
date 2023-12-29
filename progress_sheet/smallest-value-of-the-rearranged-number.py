class Solution:
    def smallestNumber(self, num: int) -> int:
        s_int=str(num)
        #check if its negative number
        if s_int[0]=='-':
            s_int=sorted(s_int[1:], reverse=True)
            return int('-'+"".join(s_int))

        else:
            s_int=sorted(s_int)
            if s_int[0]=='0':
                for i, s in enumerate(s_int):
                    if s != '0':
                        s_int[0],s_int[i]=s_int[i],s_int[0]
                        break
                return int("".join(s_int))
            else:
                return int("".join(s_int))