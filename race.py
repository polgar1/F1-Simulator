import random

class Race():
    def __init__(self, name : str, laps : int, averageLapTimeInSecs : int) -> None:
        self.name = name
        self.laps = laps
        self.avrgLapTime = averageLapTimeInSecs
    def calculateLapTime(self, driver, team):
        lapTime = self.avrgLapTime - ((driver.rating/100) * 2) - random.uniform(-(1-driver.consistency), 1-driver.consistency) - ((team.performance / 100) * 2) + driver.lapsOfFuelRemaining * 0.05
        driver.ovrTime += lapTime
        driver.lapsOfFuelRemaining -= 1
        return f"1:{lapTime-60:.5}"
    def simulateRace(self, drivers):
        for i in range(1, self.laps + 1):

            print(f"Lap {i}/{self.laps}")

            driverIndex = 0
            drivers.sort(key=lambda d: d.ovrTime)
            for driver in drivers:
                if i == 1:
                    driver.lapsOfFuelRemaining = self.laps
                x = self.calculateLapTime(driver, driver.team)

                if driverIndex != 0:
                    driver.gapToCarInFront = drivers[driverIndex-1].ovrTime - driver.ovrTime
                else:
                    driver.gapToCarInFront = 0.0

                print(f"{drivers.index(driver)+1}. {driver.name} : {x} : {driver.gapToCarInFront:.4}")
                
                driverIndex += 1
            


    
    