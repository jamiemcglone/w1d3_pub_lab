class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.food = []
        self.stock = {}

    def add_drink(self, drink, amount):
        if drink.name in self.stock.keys():
            self.stock[drink.name] += amount
        else:
            self.stock[drink.name] = amount
            self.drinks.append(drink)

    def add_food(self, food, amount):
        if food.name in self.stock.keys():
            self.stock[food.name] += amount
        else:
            self.stock[food.name] = amount
            self.drinks.append(food)

    def add_to_till(self, price):
        self.till += price

    def get_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink
            else:
                return None

    def get_food_by_name(self, food_name):
        for food in self.foods:
            if food.name == food_name:
                return food
            else:
                return None
    
    def check_customer_of_age(self, customer):
        return customer.age >= 18
        
    def check_customer_drunkenness(self, customer):
        return customer.drunkenness < 7
    
    def get_stock_value(self):
        total_stock_value = 0
        for drink in self.drinks:
            total_stock_value += drink.price * self.stock[drink.name]
        return total_stock_value

    

    

    