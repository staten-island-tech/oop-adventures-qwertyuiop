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
        while True:
                user_choice = int(input("Based on the number that corresponds with the location, where do you want to travel to?: "))
                        
                try:
                    choice = int(user_choice)
                    if 0 <= choice < len(locations):
                            break
                    else:
                        print("Error! Please enter a valid number that corresponds with the location.")
                except ValueError:
                        ("Invalid! Please try again. Enter a number.")
        if 4>choice>=0:
            return attacks[choice]['damage']
        else:
            print("Invalid choice!")
    def take_damage(self,dmg):
        self.health -= dmg
        input(f"{self.name} has taken {dmg} damage. ↓")
    


    
attacks = [

{
    "name": "Spinkick",
    "damage": 20
},

{
    "name": "Sweep kick",
    "damage": 12
},

{
    "name": "Left hook",
    "damage": 30
},

{
    "name": "Uppercut combo",
    "damage": 45
}

]








    



