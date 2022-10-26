from src.pub import Pub


class Customer:

    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def increase_drunkenness(self, alcohol_level):
        self.drunkenness += alcohol_level

    def remove_money(self, money):
        self.wallet -= money

    def buy_drink_from_pub(self, pub, drink_name):
        # find drink
        # if not too drunk and of age and drink found
        # remove price from wallet
        # add money to till
        # add drunkunness to customer
        drink_to_find = pub.get_drink_by_name(drink_name)
        sober = pub.check_customer_drunkenness(self)
        of_age = pub.check_customer_of_age(self)
        if drink_to_find and sober and of_age:
            self.remove_money(drink_to_find.price)
            pub.add_to_till(drink_to_find.price)
            self.increase_drunkenness(drink_to_find.alcohol_level)

    def decrease_drunkenness(self, rejuvenation_level):
        self.drunkenness -= rejuvenation_level

    def buy_food_from_pub(self, pub, food_name):
        food = pub.get_food_by_name(food_name)
        self.remove_money(food.price)
        pub.add_to_till(food.price)
        self.decrease_drunkenness(food.rejuvenation_level)
        
        