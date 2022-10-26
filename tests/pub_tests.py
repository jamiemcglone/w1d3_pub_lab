import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("Red Lion", 100)

    def test_pub_has_name(self):
        self.assertEqual("Red Lion", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(0, len(self.pub.drinks))

    def test_add_drink(self):
        drink = Drink("Guinness", 4.50, 1)
        self.pub.add_drink(drink, 20)
        self.assertEqual(1, len(self.pub.drinks))
        
    def test_get_drink_by_name(self):
        drink = Drink("Guinness", 4.50, 1)
        self.pub.add_drink(drink, 20)
        drink_to_find = self.pub.get_drink_by_name("Guinness")
        self.assertEqual(drink, drink_to_find)
    
    def test_customer_can_buy(self):
        customer = Customer("Romain", 10, 26, 5)
        self.assertEqual(True, self.pub.check_customer_drunkenness(customer))

    def test_customer_cannot_buy(self):
        customer = Customer("Jamie", 10, 22, 8)
        self.assertEqual(False, self.pub.check_customer_drunkenness(customer))

    def test_customer_is_old_enough(self):
        customer = Customer("Jamie", 10, 22, 4)
        result = self.pub.check_customer_of_age(customer)
        self.assertEqual(True, result)

    def test_customer_is_not_old_enough(self):
        customer = Customer("Romain", 10, 2, 4)
        result = self.pub.check_customer_of_age(customer)
        self.assertEqual(False, result)

    def test_drink_stock_non_duplicate(self):
        drink = Drink("Guinness", 4.50, 1)
        self.pub.add_drink(drink, 20)
        self.pub.add_drink(drink, 20)
        self.assertEqual(40, self.pub.stock[drink.name])
        self.assertEqual(1, len(self.pub.drinks))

    
    def test_drink_stock_duplicate(self):
        drink = Drink("Guinness", 4.50, 1)
        drink1 = Drink("Tennents", 4.50, 1)
        self.pub.add_drink(drink, 20)
        self.pub.add_drink(drink1, 20)
        self.assertEqual(2, len(self.pub.drinks))

    def test_get_stock_value(self):
        drink = Drink("Guinness", 4.50, 1)
        drink1 = Drink("Tennents", 4.50, 1)
        self.pub.add_drink(drink, 20)
        self.pub.add_drink(drink1, 20)
        self.assertEqual(180, self.pub.get_stock_value())








