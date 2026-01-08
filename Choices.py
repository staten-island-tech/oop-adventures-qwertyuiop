Main_attacks = [
{
    "name": "Spin kick",
    "damage": 5
},
{
    "name": "Sweep kick",
    "damage":2
},
{
    "name": "Left hook",
    "damage": 2
},
{
    "name": "Uppercut",
    "damage":3
}
]

def attacks():
    print("What atack do you wish to inflict?")
    for i,item in enumerate(Main_attacks):
        print (i,":",item['name'])

        