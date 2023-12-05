class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output=[""]*len(s)
        for i, char in enumerate(s):
            output[indices[i]]=char
        return "".join(output)
       
