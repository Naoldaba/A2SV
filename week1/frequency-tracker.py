class FrequencyTracker:
    def __init__(self):
        self.nums_count=defaultdict(int)
        self.frequency=defaultdict(int)

    def add(self, number: int) -> None:
        self.frequency[self.nums_count[number]]=max(0, self.frequency[self.nums_count[number]]-1)
        self.nums_count[number]+=1
        self.frequency[self.nums_count[number]]+=1

    def deleteOne(self, number: int) -> None:
        self.frequency[self.nums_count[number]]=max(0, self.frequency[self.nums_count[number]]-1)
        self.nums_count[number]=max(0, self.nums_count[number]-1)
        self.frequency[self.nums_count[number]]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency[frequency]>0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)