class Bitset:

    def __init__(self, size: int):
        self.bitset=[0]*size
        self.flipped=[1]*size
        self.size=size
        self.zeros=self.size
        self.ones=0

    def fix(self, idx: int) -> None:
        self.flipped[idx] = 0
        if self.bitset[idx] == 1:
            return
        self.bitset[idx] = 1
        self.ones += 1
        self.zeros -= 1
        
    def unfix(self, idx: int) -> None:
        self.flipped[idx] = 1
        if self.bitset[idx] == 0:
            return
        self.bitset[idx] = 0
        self.zeros += 1
        self.ones -= 1
        
    def flip(self) -> None:
        self.bitset, self.flipped= self.flipped, self.bitset
        self.zeros=self.size-self.zeros
        self.ones=self.size-self.ones

    def all(self) -> bool:
        return self.ones==self.size

    def one(self) -> bool:
        return self.ones>0

    def count(self) -> int:
        return self.ones
        
    def toString(self) -> str:
        return "".join([str(i) for i in self.bitset])
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()