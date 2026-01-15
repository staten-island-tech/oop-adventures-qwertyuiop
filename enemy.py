enemies = [

{
    "name": "Boko",
    "faction": "Boss",
    "city": "Leafy Town",
    "health": 125,
    "atk": 15,
    "attackdescription": "Boko executed a leaf hurricane that barely winded you. 15 health was lost.",
},

{
    "name":"Blue Boko",
    "faction": "Boss",
    "city": "Jumbo CIty",
    "health": 65,
    "atk": 55,
    "attackdescription":"Blue Boko threw jumbo sized machinery at you dealing a total of 55 damage.",
},

{
    "name": "Black Boko",
    "faction": "Boss",
    "city": "Death Mountain",
    "health": 85,
    "atk": 45,
    "attackdescription": "Black Boko raised the dead and skeletons swarm for 45 damage.",
},

{
    "name": "Silver Boko",
    "faction": "Boss",
    "city": "Goo Mania",
    "health": 110,
    "atk": 25,
    "attackdescription": "Silver Boko jumps and rains a gumdrop barrage. You lost 25 health.",
},

{
    "name": "Golden Boko",
    "faction": "Boss",
    "city": "Holy Sozia",
    "health": 150,
    "atk": 35,
    "attackdescription": "Moving as fast as wind, the infamous Black Boko hit a Wuxi Fingerhold that deals 35 damage.",
},

{
    "name": "Zook",
    "faction": "Boss",
    "city": "Capital Drake",
    "health": 120,
    "atk": 25,
    "attackdescription": "Zook tried to deafen your ears with Drake's Passion Fruit song but only dealt 35 damage.",
}
]
from place import *
from heroes import *
class Monsters:
    def __init__(self, name, hp,atk, description):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atkdescription = description
    def take_damage(self,dmg):
        self.hp -= dmg
        input(f"{self.name} has taken {dmg} damage. ↓")




# class Monsters():
#     def __init__(self,hp,atk):
#         self.hp = hp
#         self.atk = atk
#     def Boko(self):
#         self.hp = 125
#         self.atk = 15
#     def Boko_fight(self):
#         Heroes.health - Monsters.atk
#         print ("Boko executed a leaf hurricane that barely winded you. 15 health was lost.")
#     def Blue_Boko(self):
#         self.hp = 65
#         self.atk = 55
#     def Blue_Boko_fight(self):
#         Heroes.health - Monsters.atk
#         print ("Blue Boko threw jumbo sized machinery at you dealing a total of 55 damage.")
#     def Black_Boko(self):
#         self.hp = 85
#         self.atk = 45
#     def Black_Boko_fight(self):
#         Heroes.health - Monsters.atk
#         print ("Black Boko raised the dead and skeletons swarm for 45 damage.")
#     def Silver_Boko(self):
#         self.hp = 110
#         self.atk = 25
#     def Silver_Boko_fight(self):
#         Heroes.health - Monsters.atk
#         print ("Silver Boko jumps and rains a gumdrop barrage. You lost 25 health.")
#     def Golden_Boko(self):
#         self.hp = 150
#         self.atk = 35
#     def Golden_Boko_fight(self):
#         Heroes.health - Monsters.atk
#         print ("Moving as fast as wind, the infamous Black Boko hit a Wuxi Fingerhold that deals 35 damage.")
#     def Zook(self):
#         self.hp = 115
#         self.atk = 25
#     def Zook_fight(self):
#         Heroes.health - Monsters.atk
#         print ("Zook tried to deafen your ears with Drake's Passion Fruit song but only dealt 35 damage.")