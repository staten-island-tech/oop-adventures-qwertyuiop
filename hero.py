class Protagnist:
    def __init__(self,name):
        self.name = name
        self.health = 1000
        self.stamina = 1000
        print (f"Here are {name}'s stats: Health:{self.health}, Stamina:{self.stamina}")
    def Zelda(self):
        self.name = "Zelda"
        self.health = 1000
        self.stamina = 1000
name = input("What is your character's name?:")
self = Protagnist(f"{name}")





