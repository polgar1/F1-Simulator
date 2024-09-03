import random

class Race():
    def __init__(self, name, laps, averageLapTimeInSecs) -> None:
        self.name = name
        self.laps = laps
        self.avrgLapTime = averageLapTimeInSecs
    def calculateLapTime(self, driver, team):
        lapTime = self.avrgLapTime - ((driver.rating/100) * 2 * random.uniform(-0.25, 0.25)) - ((team.performance / 100) * 2)
        driver.ovrTime += lapTime
        return f"1:{lapTime-60:.5}"
    def simulateRace(self, drivers):
        for i in range(1, self.laps + 1):
            print(f"Lap {i}")
            driverIndex = 0
            for driver in drivers:
                x = self.calculateLapTime(driver, driver.team)

                if driverIndex != 0:
                    driver.gapToCarInFront = drivers[driverIndex-1].ovrTime - driver.ovrTime
                else:
                    driver.gapToCarInFront = 0.0

                print(f"{drivers.index(driver)+1}. {driver.name} : {x} : {driver.gapToCarInFront:.4}")
                driver.gapToCarInFront = drivers
                
                driverIndex += 1
            drivers.sort(key=lambda d: d.ovrTime)


    
    