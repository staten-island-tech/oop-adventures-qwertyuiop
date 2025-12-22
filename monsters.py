class Antagonist:
    def Bison(self, name):
        self.name = "M. Bison"
        self.health = 100
        self.stamina = 100
print("Choose a character: Ryu, Ken, Sagat, M. Bison")
name = input("What would you like to choose?: ")
characters = Antagonist()
if name == "M. Bison":
    print(characters.Bison(name))
        
