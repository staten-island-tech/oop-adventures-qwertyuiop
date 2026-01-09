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

class Map:
    def location():
        print("Welcome to the world of Doria, the land of the surprises and evil. Where do you want to explore first traveler?")
        for index, item in enumerate(locations):
            print(index, ":", item["name"])
        choice = int(input("According to the number that accomodates the location, where do you want to go? "))
        if choice == 0:
            print("Going to Leafy Town!")
        elif choice == 1:
            print("Going to Jumbo City!")
        elif choice == 2:
            print("Going to Death Mountain!")
        elif choice == 3:
            print("Going to Goo Mania!")
        elif choice == 4:
            print("Going to Holy Sozia!")
        elif choice == 5:
            print("Going to Capital Drake!")
        else:
            print("Error! Please enter the number that accomodates the location of where you want to go!")
    location()