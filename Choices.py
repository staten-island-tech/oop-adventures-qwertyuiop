Main_attacks = [
{
    "name": "Spin kick",
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
    "damage":30
}
]

def attacks():
    print("What atack do you wish to inflict?")
    for i,item in enumerate(Main_attacks):
        print (i,":",item['name'])
