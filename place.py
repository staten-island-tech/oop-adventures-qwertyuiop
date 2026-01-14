locations = [

{
    "name": "Leafy Town",
    "description": "Leafy Town is the place where nature prospers. The land of Doria's natural beauty. Great adventures around farms and forests await you here."
},

{
    "name": "Jumbo City",
    "description": "Jumbo City is a metro city full of enlarged objects and buildings. Interactions within this city may become weird, but the adventures are outstanding!"
},

{
    "name": "Death Mountain",
    "description": "Death Mountain is nothing like a warm paradise, suitable for vacational needs. Its volcanic magma can burn the flesh of any species. Beware of the heat, venture further within its crater, and overcome death."
},

{
    "name": "Goo Mania",
    "description": "Goo Mania is a city full of ink, gum, and slime. Be careful of where you are stepping, or you may step in a puddle of goo you can't take off your boots. It may be a sticky adventure, but it's definitely a tasty one."
},

{
    "name": "Holy Sozia",
    "description": "Holy Sozia is the forest of faries and angels. When walking on the trails, you are bound to hear angels whispering and singing."
},

{
    "name": "Capital Drake",
    "description": "Capital Drake looks almost identical to cities found in Canada. You can find statues of Drake and his music around the whole capital."
}
]
from heroes import *
class Map:
    def __init__(self):
        self.monster = Monsters()
    def rounds(self,x):
        while Heroes.health > 0 and self.monster.hp > 0:
            Attacks.show_attacks
            x()
    def location(self):
        print("Welcome to the world of Doria, the land of the surprises and evil. Where do you want to explore first traveler?")
        for index, item in enumerate(locations):
            print(index, ":", item["name"])
        choice = int(input("According to the number that accomodates the location, where do you want to go?: "))
        if choice == 0:
            print("Going to Leafy Town! You are about to fight Boko!")
            self.monster.Boko()
            self.rounds(self.monster.Boko_fight)
        elif choice == 1:
            print("Going to Jumbo City! You are going to fight Blue Boko!")
            self.monster.Blue_Boko()
            self.rounds(self.monster.Blue_Boko_fight)
        elif choice == 2:
            print("Going to Death Mountain! You are going to fight Black Boko")        
            self.monster.Black_Boko()
            self.rounds(self.monster.Black_Boko_fight)
        elif choice == 3:
            print("Going to Goo Mania! You are going to fight Silver Boko")
            self.monster.Silver_Boko()
            self.rounds(self.monster.Silver_Boko_fight)
        elif choice == 4:
            print("Going to Holy Sozia! You are going to fight Golden Boko!")
            self.monster.Golden_Boko()
            self.rounds(self.monster.Golden_Boko_fight)
        elif choice == 5:
            print("Going to Capital Drake! You are about to fight Zook")
            self.monster.Zook()
            self.rounds(self.monster.Zook_fight)
        else:
            print("Error! Please enter the number that accomodates the location of where you want to go!")
    location()