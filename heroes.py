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

    def show_attacks(self):
        print("What attack do you want to execute?")
        for i, item in enumerate(self.attacks):
            print(i, ":", item['name'])





