class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        k=Max=0
        for i in range(len(processorTime)):
            for j in range(k, k+4):
                Max=max(Max, processorTime[i]+tasks[j])
            k+=4
        return Max