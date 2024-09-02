import random

class Race():
    def __init__(self, name, laps, averageLapTimeInSecs) -> None:
        self.name = name
        self.laps = laps
        self.avrgLapTime = averageLapTimeInSecs
    def calculateLapTime(self, driver, team):
        lapTime = self.avrgLapTime - ((driver.rating/100) * 2 * (random.randrange(-25, 25) / 100)) - ((team.performance / 100) * 2)
        return lapTime
    def simulateRace(self, drivers):
        for i in range(1, self.laps + 1):
            print("Lap", i)
            for driver in drivers:
                x = drivers[driver]
                print(driver, ":", self.calculateLapTime(x, x.team))


    
    