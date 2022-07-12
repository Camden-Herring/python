# class User:
#     def __init__(self):
#         self.first_name = "Ada"
#         self.last_name = "Lovelace"
#         self.age = 42

# print("Hello!")

# user_ada = User()



from random import randint


class Zombie:
    def __init__(self):

        self.strength = self.assign_strength 
        self.weapon = self.assign_weapon
    
    def assign_weapon(self):
        
        weapons = [
            "knife",
            "machete",
            "sword",
            "claws",
            "bite",
            "bat",
            "hammer",
            "blowtorch"
        ]

        return weapons[randint(0,len(weapons) - 1)]

    def assign_strength(self):
        return randint(0,10)

my_zombie = Zombie()
# print(my_zombie.strength())
# print(my_zombie.weapon())

zombie_num = randint(1,20)

print(f"Oh snap! There are {zombie_num} zombies coming our way! Here are their stats:")

for zombies in range(zombie_num):
    new_zombie = Zombie()
    # print(my_zombie.strength())
    # print(my_zombie.weapon())
    print(f"zombie #{zombies+1} has a {my_zombie.weapon()}, and has a strength level of {my_zombie.strength()}")

