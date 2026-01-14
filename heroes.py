class Heroes:
    def __init__(self):
        self.name="YoYo"
        self.health = 120
        self.faction= "Champion"
        self.description = "YoYo is a legendary warrior who was chosen to be Lumy's knight in shining armor. However, the champion has just awoken from his deep slumber."
    

    
    
attacks = [

{
    "name": "Spinkick",
    "atk": 15
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
class Attacks():
    def show_attacks():
        print("What attack do you want to execute?")
        for i, item in enumerate(attacks):
            print(i, ":", item['name'])
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("You used spinkick! You dealt 15 damage!")
        elif choice == 1:
            print("You used sweep kick! You dealt 8 damage!")
        elif choice == 2:
            print("You used left hook! You dealt 25 damage!")
        elif choice == 3:
            print("You used uppercut combo! You dealt 30 damage!")
        else:
            print("Invalid choice!")
    show_attacks()



class Monsters():
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk
    def Boko(self):
        self.hp = 125
        self.atk = 15
    def Boko_fight(self):
        Heroes.health - Monsters.atk
        print ("Boko executed a leaf hurricane that barely winded you. 15 health was lost.")
    def Blue_Boko(self):
        self.hp = 65
        self.atk = 55
    def Blue_Boko_fight(self):
        Heroes.health - Monsters.atk
        print ("Blue Boko threw jumbo sized machinery at you dealing a total of 55 damage.")
    def Black_Boko(self):
        self.hp = 85
        self.atk = 45
    def Black_Boko_fight(self):
        Heroes.health - Monsters.atk
        print ("Black Boko raised the dead and skeletons swarm for 45 damage.")
    def Silver_Boko(self):
        self.hp = 110
        self.atk = 25
    def Silver_Boko_fight(self):
        Heroes.health - Monsters.atk
        print ("Silver Boko jumps and rains a gumdrop barrage. You lost 25 health.")
    def Golden_Boko(self):
        self.hp = 150
        self.atk = 35
    def Golden_Boko_fight(self):
        Heroes.health - Monsters.atk
        print ("Moving as fast as wind, the infamous Black Boko hit a Wuxi Fingerhold that deals 35 damage.")
    def Zook(self):
        self.hp = 115
        self.atk = 25
    def Zook_fight(self):
        Heroes.health - Monsters.atk
        print ("Zook tried to deafen your ears with Drake's Passion Fruit song but only dealt 35 damage.")








