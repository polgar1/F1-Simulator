from race import Race

class Driver():
    def __init__(self, name, rating, team, consistency) -> None:
        self.rating = rating
        self.name = name
        self.gapToCarInFront = 0.2
        self.team = team
        self.ovrTime = 0
        self.consistency = consistency #0.1-1.0
        self.lapsOfFuelRemaining = 0

class Team():
    def __init__(self, name, performance) -> None:
        self.performance = performance
        self.name = name

#REDBULL
redBull = Team("Redbull Racing", 90)
verstappen = Driver("Max Verstappen", 99, redBull, 0.9)
perez = Driver("Sergio Perez", 73, redBull, 0.8)


#MCLAREN
mclaren = Team("Mclaren", 99)
norris = Driver("Lando Norris", 90, mclaren, 0.8)
piastri = Driver("Oscar Piastri", 88, mclaren, 0.8)


#Ferrari
ferrari = Team("Ferrari", 92)
leclerc = Driver("Charles Leclerc", 93, ferrari, 0.7)
sainz = Driver("Carlos Sainz", 85, ferrari, 0.8)


#Mercedes
mercedes = Team("Mercedes", 90)
hamilton = Driver("Lewis Hamilton", 93, mercedes, 0.8)
russell = Driver("Geroge Russell", 91, mercedes, 0.7)


#Aston Martin
astonMartin = Team("Aston Martin", 45)
alonso = Driver("Fernando Alonso", 80, astonMartin, 0.7)
stroll = Driver("Lance Stroll", 56, astonMartin, 0.4)


#Williams
williams = Team("Williams", 44)
albon = Driver("Alexander Albon", 52, williams, 0.8)
colapinto = Driver("Franco Colapinto", 4, williams, 0.5)


#Haas 
haas = Team("Haas", 34)
magnussen = Driver("Kevin Magnussen", 48, haas, 0.1)
hulkenberg = Driver("Nico Hülkenberg", 64, haas, 0.4)


#Alpine
alpine = Team("Alpine", 34)
gasly = Driver("Pierre Gasly", 60, alpine, 0.5)
ocon = Driver("Esteban Ocon", 60, alpine, 0.5)


#RB
vcarb = Team("VCARB", 30)
tsunoda = Driver("Yuki Tsunoda", 40, vcarb, 0.1)
ricciardo = Driver("Daniel Ricciardo", 40, vcarb, 0.1)


#Sauber
sauber = Team("Sauber", 1)
bottas = Driver("Valtteri Bottas", 20, sauber, 0.5)
zhou = Driver("Guanyu Zhou", 1, sauber, 0.5)


teams = [redBull, mclaren, ferrari, mercedes, astonMartin, williams, haas, alpine, vcarb, sauber]
drivers = [verstappen, perez, norris, piastri, leclerc, sainz, hamilton, russell, alonso, stroll, albon, colapinto, magnussen, hulkenberg, gasly, ocon,
           tsunoda, ricciardo, bottas, zhou]


bahrain = Race("Bahrain", 57, 94)

bahrain.simulateRace(drivers)