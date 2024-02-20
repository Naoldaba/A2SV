
class MyCircularQueue:

    def __init__(self, k: int):
        self.circle_queue=deque()
        self.k=k
        
    def enQueue(self, value: int) -> bool:
        if len(self.circle_queue)==self.k:  
            return False
        self.circle_queue.append(value)
        return True
        
    def deQueue(self) -> bool:
        if len(self.circle_queue)==0: 
            return False
        self.circle_queue.popleft()
        return True
        
    def Front(self) -> int:
        if len(self.circle_queue)==0:
            return -1
        return self.circle_queue[0]
        
        
    def Rear(self) -> int:
        if len(self.circle_queue)==0:
            return -1
        return self.circle_queue[-1]
        
    def isEmpty(self) -> bool:
        return len(self.circle_queue)==0
        
    def isFull(self) -> bool:
        return len(self.circle_queue)==self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()