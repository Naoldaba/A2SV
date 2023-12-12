class UndergroundSystem:
    def __init__(self):
        self.start=defaultdict(tuple)
        self.end=defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id]=(t,stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starttime,startstation=self.start[id]
        total=t-starttime
        self.end[(startstation,stationName)].append(total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.end[(startStation,endStation)])/len(self.end[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)