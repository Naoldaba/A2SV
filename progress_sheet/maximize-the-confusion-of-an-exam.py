class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count_true=0
        count_false=0
        Max=l=0
        for r in range(len(answerKey)):
            if answerKey[r]=="T":
                count_true+=1
            else:
                count_false+=1
            while min(count_true, count_false)>k:
                if answerKey[l]=="T":
                    count_true-=1
                else:
                    count_false-=1
                l+=1
            Max=max(Max, r-l+1)
        return Max