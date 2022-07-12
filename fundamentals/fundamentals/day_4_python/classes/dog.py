from classes.animal import Animal

class Dog(Animal):
    def __init__ (self, name, owner, breed, color):
        super().__init__(name, owner, breed)
        self.breed = breed
        self.color = color

    # Overriding!!!!!!!!!!!!!!!!!

    def print_info(self):
        super().print_info()
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")

    def walk_animal(self):
        print("Im a dog so i need to be walked twice a day")

