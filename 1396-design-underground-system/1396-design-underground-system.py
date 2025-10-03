class UndergroundSystem:

    def __init__(self):
        self.total_time = defaultdict(list)
        self.checkins = {}
        self.checkouts = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)       

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.checkouts[id] = (stationName, t) 

        key = (self.checkins[id][0], stationName)
        time = self.checkouts[id][1] - self.checkins[id][1]

        self.total_time[key].append(time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.total_time[(startStation, endStation)]
        length = len(self.total_time[(startStation, endStation)])
        avg = sum(times) / length

        return avg


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)