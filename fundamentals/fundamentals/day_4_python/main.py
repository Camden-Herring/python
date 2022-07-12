
from classes.animal import Animal
from classes.dog import Dog
from classes.cat import Cat

# max = Animal("Max", "Alex", "labrador")
# max.print_info()

# jagger = Dog("Jagger", "Alfredo", "Golden retriever", "Golden")
# jagger.print_info()
# jagger.walk_animal()

# chester = Cat("Chester", "Alfredo", "Yellow", 6)
# chester.print_info()
# chester.walk_animal()

# first_name = input("Please give me your first name: ")

# print(f"It's nice to meet you {first_name}!")

# print("0) EXIT this program?")
# print("1) Add a Cat!")
# print("2) Add a Dog!")
option = input ("Select an option")

while option != '0':
    if option == '1':
        name = input( "name of your cat: ")
        owner = input("who is the owner?")
        breed = input("what is the breed?")
        age = input("what is the age your cat?")
        new_cat = Cat(name, owner, breed, age)
    elif option == '2':
        name = input('what is the name? ')
        owner = input("who is the owner? ")
        breed = input("what is the breed? ")
        color = input("what is the color? ")

    print("0) EXIT this program?")
    print("1) Add a Cat!")
    print("2) Add a Dog!")
    option = input ("Select and option: ")
