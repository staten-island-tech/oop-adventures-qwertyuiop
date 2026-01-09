Monsters = [
{
    "name": "Boko",
    "faction": "Mini-Boss",
    "city": "Leafy Town",
    "health": 45,
    "atk": 5
},

{
    "name":"Blue Boko",
    "faction": "Boss",
    "city": "Jumbo CIty",
    "health": 65,
    "atk": 15
},

{
    "name": "Black Boko",
    "faction": "Boss",
    "city": "Death Mountain",
    "health": 85,
    "atk": 20
},

{
    "name": "Silver Boko",
    "faction": "Boss",
    "city": "Goo Mania",
    "health": 110,
    "atk": 25
},

{
    "name": "Golden Boko",
    "faction": "Boss",
    "city": "Holy Sozia",
    "health": 150,
    "atk": 35
},

{
    "name": "Zook",
    "faction": "Mini-Boss",
    "city": "Capital Drake",
    "health": 35,
    "atk":3
}
]

class Monsters():
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk
    def Boko_fight(self):
        self.hp = 45
        self.atk = 5
        print ("Boko executed a leaf hurricane that barely winded you. 5 health was lost.")
    def Blue_Boko_fight(self):
        self.hp = 65
        self.atk = 15
        print ("Blue Boko threw jumbo sized machinery at you dealing a total of 15 damage.")
    def Black_Boko_fight(self):
        self.hp = 85
        self.atk = 20
        print ("Black Boko raised the dead and skeletons swarm for 20 damage.")
    def Silver_Boko_fight(self):
        self.hp = 110
        self.atk = 25
        print ("Silver Boko jumps and rains a gumdrop barrage. You lost 25 health.")
    def Golden_Boko_fight(self):
        self.hp = 150
        self.atk = 35
        print ("Moving as fast as wind, the infamous Black Boko ")
    def Zook_fight(self):
        self.hp = 35
        self.atk = 3

 



