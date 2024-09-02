from race import Race

class Driver():
    def __init__(self, name, rating, team) -> None:
        self.rating = rating
        self.name = name
        self.driverInFront = 0
        self.gapToCarInFront = 0.2
        self.team = team

class Team():
    def __init__(self, name, performance) -> None:
        self.performance = performance
        self.name = name

#REDBULL
redBull = Team("Redbull Racing", 90)
verstappen = Driver("Max Verstappen", 99, redBull)
perez = Driver("Sergio Perez", 66, redBull)


#MCLAREN
mclaren = Team("Mclaren", 99)
norris = Driver("Lando Norris", 90, mclaren)
piastri = Driver("Oscar Piastri", 88, mclaren)


#Ferrari
ferrari = Team("Ferrari", 92)
leclerc = Driver("Charles Leclerc", 93, ferrari)
sainz = Driver("Carlos Sainz", 85, ferrari)


#Mercedes
mercedes = Team("Mercedes", 90)
hamilton = Driver("Lewis Hamilton", 93, mercedes)
russell = Driver("Geroge Russell", 91, mercedes)


#Aston Martin
astonMartin = Team("Aston Martin", 50)
alonso = Driver("Fernando Alonso", 80, astonMartin)
stroll = Driver("Lance Stroll", 56, astonMartin)


#Williams
williams = Team("Williams", 44)
albon = Driver("Alexander Albon", 52, williams)
colapinto = Driver("Franco Colapinto", 48, williams)


#Haas 
haas = Team("Haas", 34)
magnussen = Driver("Kevin Magnussen", 48, haas)
hulkenberg = Driver("Nico Hülkenberg", 64, haas)


#Alpine
alpine = Team("Alpine", 34)
gasly = Driver("Pierre Gasly", 60, alpine)
ocon = Driver("Esteban Ocon", 60, alpine)


#RB
vcarb = Team("VCARB", 30)
tsunoda = Driver("Yuki Tsunoda", 40, vcarb)
ricciardo = Driver("Daniel Ricciardo", 40, vcarb)


#Sauber
sauber = Team("Sauber", 1)
bottas = Driver("Valtteri Bottas", 20, sauber)
zhou = Driver("Guanyu Zhou", 1, sauber)


teams = [redBull, mclaren, ferrari, mercedes, astonMartin, williams, haas, alpine, vcarb, sauber]
drivers = {"Max Verstappen" : verstappen, "Sergio Perez" : perez, "Lando Norris" : norris, "Oscar Piastri" : piastri, "Charles Leclerc" : leclerc,
           "Carlos Sainz" : sainz, "Lewis Hamilton" : hamilton, "George Russell" : russell, "Fernando Alonso" : alonso, "Lance Stroll" : stroll,
           "Alexander Albon" : albon, "Franco Colapinto" : colapinto, "Kevin Magnussen" : magnussen, "Nico Hulkenberg" : hulkenberg, "Pierre Gasly" : gasly,
           "Esteban Ocon" : ocon, "Yuki Tsunoda" : tsunoda, "Daniel Ricciardo" : ricciardo, "Valtteri Bottas" : bottas, "Guanyu Zhou": zhou}


bahrain = Race("Bahrain", 57, 92)

bahrain.simulateRace(drivers)