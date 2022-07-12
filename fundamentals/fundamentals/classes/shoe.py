class Shoe:

    def __init__(self, brand, shoe_type, price):

        self.brand = brand
        self.shoe_type = shoe_type
        self.price = price

        self.instock = True
    
    def on_sale_by_percent(self, percent):
        self.price = self.price * (1 - percent)


skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)

skater_shoe.on_sale_by_percent(0.2)
print(skater_shoe.price)



# 
# 
# 
# 
# 
# 
# skater_shoe.price = (1 - 0.2) * skater_shoe.price

# dress_shoe.price = dress_shoe.price * (1 - 0.1)

# skater_shoe.price = skater_shoe.price * (1 - 0.1)