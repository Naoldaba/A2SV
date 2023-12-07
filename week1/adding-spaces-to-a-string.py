class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result=""
        prev_ind=0
        for i in spaces:
          result+=s[prev_ind:i]
          result+=" "
          prev_ind=i
        result+=s[prev_ind:]
        return result