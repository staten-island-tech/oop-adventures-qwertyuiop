from heroes import *
from place import *
from enemy import *
class Game:
        Protaganist = Heroes("YoYo", 150, "Champion", "YoYo is a legendary warrior who was chosen to be Lumy's knight in shining armor. However, the champion has just awoken from his deep slumber.")
        Protaganist.health_reset = Protaganist.health
        defeated_monster = set()
        while Protaganist.health > 0 and len(defeated_monster) < len(locations):
                for i, item in enumerate(locations):
                        status = " Defeated" if item['name'] in defeated_monster else " Undefeated"
                        print(i, ":", item['name'] + status)
                while True:
                        user_choice = input("Based on the number that corresponds with the location, where do you want to travel to?: ")
                        
                        try:
                                choice = int(user_choice)
                                if 0 <= choice < len(locations):
                                        break
                                else:
                                        print("Error! Please enter a valid number that corresponds with the location.")
                        except ValueError:
                                print("Invalid! Please try again. Enter a number.")
                
                if 0 <= choice < len(locations) and locations[choice]['name'] not in defeated_monster:

                        input(f"You are headed to {locations[choice]['name']}. ↓") 
                        input(f"{locations[choice]['description']} ↓") 
                        input(f"{enemies[choice]['name']} has appeared. ↓")
                        
                        mob = Monsters(enemies[choice]['name'], enemies[choice]['health'], enemies[choice]['atk'], enemies[choice]['attackdescription'])     
                
                        while Protaganist.health > 0 and mob.hp > 0:
                                print(f"{mob.name}: {mob.hp}")
                                print(f"{Protaganist.name}: {Protaganist.health}")
                                
                                hero_attacks  = Heroes.show_attacks()
                                Monsters.take_damage(mob, hero_attacks)

                                if mob.hp <= 0:
                                        print(f"You have defeated {mob.name}! ↓")
                                        defeated_monster.add(locations[choice]['name'])
                                        Protaganist.health = Protaganist.health_reset
                                        break
                                
                                Heroes.take_damage(Protaganist, mob.atk)
                elif 0 <= choice < len(locations) and locations[choice]['name'] in defeated_monster:
                        print("You have already defeated the boss in this location. Please choose another location.")
                else:
                        print("Error! Please enter the number that accomodates the location of where you want to go!")
        if len(defeated_monster) == len(locations):
                print("Congratulations! You have conquered all the bosses and saved Doria!")
        elif Protaganist.health <=0:
                print("You have been defeated! You were too weak to save Doria. Game Over.")
        
