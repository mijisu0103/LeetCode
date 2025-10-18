from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.checkIns = {}
        self.routes = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, t0 = self.checkIns.pop(id)
        dt = t - t0
        total, cnt = self.routes[(startStation, stationName)]
        self.routes[(startStation, stationName)] = [total + dt, cnt + 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, cnt = self.routes[(startStation, endStation)]
        return total / cnt