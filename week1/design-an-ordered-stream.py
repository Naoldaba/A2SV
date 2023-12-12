class OrderedStream:

    def __init__(self, n: int):
        self.values = [0]*n
        self.n = n
        self.pointer = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey-1] = value
        
        temp = []
        while self.pointer < self.n and self.values[self.pointer] != 0:
            temp.append(self.values[self.pointer])
            self.pointer += 1
        return temp