import unittest

from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jamie", 10, 22, 2)
        self.customer2 = Customer("Romain", 10, 26, 9)
        self.customer3 = Customer("Romain", 10, 10, 0)

    def test_customer_has_a_name(self):
        self.assertEqual("Jamie", self.customer.name)

    def test_customer_has_a_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    def test_customer_has_a_age(self):
        self.assertEqual(22, self.customer.age)

    def test_customer_has_a_drunkenness(self):
        self.assertEqual(2, self.customer.drunkenness)

    def test_customer_remove_money(self):
        self.customer.remove_money(5)
        self.assertEqual(5, self.customer.wallet)

    def test_customer_can_buy_drink(self):
        drink = Drink("Guinness", 4, 1)
        pub = Pub("Red Lion", 100)
        pub.add_drink(drink, 20)
        self.customer.buy_drink_from_pub(pub, "Guinness")
        self.assertEqual(3, self.customer.drunkenness)
        self.assertEqual(104, pub.till)
        self.assertEqual(6, self.customer.wallet)
    
    def test_customer_cannot_buy_too_drunk(self):
        drink = Drink("Guinness", 4, 1)
        pub = Pub("Red Lion", 100)
        pub.add_drink(drink, 20)
        self.customer2.buy_drink_from_pub(pub, "Guinness")
        self.assertEqual(9, self.customer2.drunkenness)
        self.assertEqual(100, pub.till)
        self.assertEqual(10, self.customer2.wallet)

    def test_customer_cannot_buy_too_young(self):
        drink = Drink("Guinness", 4, 1)
        pub = Pub("Red Lion", 100)
        pub.add_drink(drink, 20)
        self.customer3.buy_drink_from_pub(pub, "Guinness")
        self.assertEqual(0, self.customer3.drunkenness)
        self.assertEqual(100, pub.till)
        self.assertEqual(10, self.customer3.wallet)

    def test_customer_cannot_find_drink(self):
        drink = Drink("Guinness", 4, 1)
        pub = Pub("Red Lion", 100)
        pub.add_drink(drink, 20)
        self.customer.buy_drink_from_pub(pub, "Tennents")
        self.assertEqual(2, self.customer.drunkenness)
        self.assertEqual(100, pub.till)
        self.assertEqual(10, self.customer.wallet)

    




