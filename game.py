from place import Map
from heroes import Attacks, Monsters

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

enemies = [

{
    "name": "Boko",
    "faction": "Boss",
    "city": "Leafy Town",
    "health": 125,
    "atk": 15
    "attackdescription": "Boko executed a leaf hurricane that barely winded you. 15 health was lost."
},

{
    "name":"Blue Boko",
    "faction": "Boss",
    "city": "Jumbo CIty",
    "health": 65,
    "atk": 55
    "attackdescription":"Blue Boko threw jumbo sized machinery at you dealing a total of 55 damage."
},

{
    "name": "Black Boko",
    "faction": "Boss",
    "city": "Death Mountain",
    "health": 85,
    "atk": 45
    "attackdescription": "Black Boko raised the dead and skeletons swarm for 45 damage."
},

{
    "name": "Silver Boko",
    "faction": "Boss",
    "city": "Goo Mania",
    "health": 110,
    "atk": 25
    "attackdescription": "Silver Boko jumps and rains a gumdrop barrage. You lost 25 health."
},

{
    "name": "Golden Boko",
    "faction": "Boss",
    "city": "Holy Sozia",
    "health": 150,
    "atk": 35
    "attackdescription": "Moving as fast as wind, the infamous Black Boko hit a Wuxi Fingerhold that deals 35 damage."
},

{
    "name": "Zook",
    "faction": "Boss",
    "city": "Capital Drake",
    "health": 120,
    "atk": 25
    "attackdescription": "Zook tried to deafen your ears with Drake's Passion Fruit song but only dealt 35 damage."
}
]

class Map:
    def __init__(self):
        self.monster = Monsters()
    def show_attacks():
        print("What attack do you want to execute?")
        for i, item in enumerate(attacks):
            print(i, ":", item['name'])
        choice = int(input("Enter your choice: "))
        if 4>choice>=0:
            print(f"You used {attacks[choice]["name"]}! You dealt {attacks[choice]["damage"]}!")
        else:
            print("Invalid choice!")