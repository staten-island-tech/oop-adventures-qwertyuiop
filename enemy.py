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

