class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        queue=deque([i for i in range(len(tickets))])
        time=0
        while queue:
            for i in range(len(queue)):
                
                pos=queue.popleft()
                tickets[pos]-=1
                if tickets[pos]>=1:
                    queue.append(pos)
                time+=1
                if tickets[k]==0:
                    return time

        