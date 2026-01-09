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



