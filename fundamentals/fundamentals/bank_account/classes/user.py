

from bank_account import Bank_account


class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):


        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
        self.account = Bank_account(int_rate = 0.02, balance = 0)
    
    def display_info(self):

        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"{self.first_name} {self.last_name}, is now a rewards member. 200 points has been added to their Gold Card Points!")
        else:
            print(f"{self.first_name}, is already a rewards member!")

    def spend_points(self, amount):

        if self.gold_card_points-amount > 0:
            self.gold_card_points -= amount
            print(f"{self.gold_card_points} points remaining for Gold Card Balance")
        else:
            print(f"{self.first_name} does not have enough points!")

    def make_deposit(self, amount):
        self.account.deposit(amount)
        # print(repr(self.account))

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        # print(repr(self.account))

    def display_user_balance(self):
        print(f"Your balance is: ${self.account.balance}")



user_camden = User("Camden", "Herring", "camdenherring1103@gmail.com", 18)
user_camden.make_deposit(1150)
user_camden.make_withdrawal(1000)
user_camden.display_user_balance()
# user_camden.spend_points(50)
# # spend points works

# # user_camden.enroll()
# # enroll works

# user_camden.spend_points(150)

# user_simon = User("Simon", "Herring", "simonherring@gmail.com", 50)

# user_simon.display_info()
# user_camden.display_info()
# # display info works

# # user_camden.enroll()
# # logic works for the enrollment


