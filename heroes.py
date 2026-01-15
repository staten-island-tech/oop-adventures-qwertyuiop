from enemy import *
class Heroes:
    def __init__(self, name, health, faction, description):
        self.name= name
        self.health = health
        self.faction = faction
        self.description = description
    def show_attacks():
        print("What attack do you want to execute?")
        for i, item in enumerate(attacks):
            print(i, ":", item['name'])
        choice = int(input("Enter your choice: "))
        if 4>choice>=0:
            return attacks[choice]["damage"]
        else:
            print("Invalid choice!")
    def take_damage(self,dmg):
        self.health -= dmg
        input(f"{self.name} has taken {dmg} damage. ↓")
    


    
attacks = [

{
    "name": "Spinkick",
    "damage": 15
},

{
    "name": "Sweep kick",
    "damage": 8
},

{
    "name": "Left hook",
    "damage": 25
},

{
    "name": "Uppercut combo",
    "damage": 30
}

]








    



