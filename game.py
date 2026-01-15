from heroes import *
from place import *
from enemy import *
class Game:
        Protaganist = Heroes("YoYo", 120, "Champion", "YoYo is a legendary warrior who was chosen to be Lumy's knight in shining armor. However, the champion has just awoken from his deep slumber.")
        for i, item in enumerate(locations):
                print(i, ":", item['name'])
        choice = int(input("What location do you want to travel to?: "))
        if 6>choice>=0:
                input(f"You are headed to {locations[choice]["name"]}. ↓") 
                input(f"{locations[choice]['description']} ↓") 
                input(f"{enemies[choice]["name"]} has appeared. ↓")
                mob = Monsters(enemies[choice]["name"], enemies[choice]["health"], enemies[choice]["atk"], enemies[choice]["attackdescription"])     
        else:
                print("Error! Please enter the number that accomodates the location of where you want to go!")
        while Protaganist.health > 0 and mob.hp > 0:
                print(f"{mob.name}: {mob.hp}")
                print(f"{Protaganist.name}: {Protaganist.health}")
                hero_attacks  = Heroes.show_attacks()
                Monsters.take_damage(mob, hero_attacks)
                Heroes.take_damage(Protaganist, mob.atk)
        