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
        if 4>choice>=0:
            print(f"You used {attacks[choice]["name"]}! You dealt {attacks[choice]["damage"]}!")
        else:
            print("Invalid choice!")