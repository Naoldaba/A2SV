class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.length=0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.stack2=list(reversed(self.stack1))
        self.length+=1
    def pop(self) -> int:
        print(self.stack1)
        print(self.stack2)
        if self.length>0:
            temp = self.stack2.pop()
            self.stack1=list(reversed(self.stack2))
            self.length-=1
            return temp
        return -1

    def peek(self) -> int:
        return self.stack1[0]
    def empty(self) -> bool:
        return True if self.length==0 else False

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()