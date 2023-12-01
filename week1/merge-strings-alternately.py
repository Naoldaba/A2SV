class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        nw_st=""
        for i in range(len(min(word1, word2, key=len))):
            temp=word1[i]+word2[i]
            nw_st+=temp
        Max=max(word1,word2, key=len)
        if len(word1)!=len(word2):
            nw_st+=Max[len((min(word1, word2, key=len))):]
        return nw_st
