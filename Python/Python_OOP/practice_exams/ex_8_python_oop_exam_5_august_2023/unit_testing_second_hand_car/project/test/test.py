from unittest import TestCase, main

from project.second_hand_car import SecondHandCar

class SecondHandCarTest(TestCase):

    def setUp(self):
        self.car = SecondHandCar("model", "test_type", 200, 5000.50)


    def test_init_to_default(self):
        self.assertEqual("model", self.car.model)
        self.assertEqual("test_type", self.car.car_type)
        self.assertEqual(200, self.car.mileage)
        self.assertEqual(5000.50, self.car.price)
        self.assertFalse(self.car.repairs)

    def test_init_types(self):
        self.assertIsInstance(self.car.model, str)
        self.assertIsInstance(self.car.car_type, str)
        self.assertIsInstance(self.car.mileage, int)
        self.assertIsInstance(self.car.price, float)
        self.assertIsInstance(self.car.repairs, list)


    def test_price_raise_value_error_less_then_1(self):
        with self.assertRaises(ValueError) as err:
            self.car.price = 0.99
        self.assertEqual("Price should be greater than 1.0!", str(err.exception))

    def test_price_raise_value_error_equal_1(self):
        with self.assertRaises(ValueError) as err:
            self.car.price = 1.00
        self.assertEqual("Price should be greater than 1.0!", str(err.exception))

    def test_mileage_raise_value_error_equal_100(self):
        with self.assertRaises(ValueError) as err:
            self.car.mileage = 100
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(err.exception))

    def test_mileage_raise_value_error_less_100(self):
        with self.assertRaises(ValueError) as err:
            self.car.mileage = 99.99
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(err.exception))

    def test_promotional_price_raise_value_error_new_price_greater_then_price(self):
        with self.assertRaises(ValueError) as err:
            self.car.set_promotional_price(5001)
        self.assertEqual("You are supposed to decrease the price!", str(err.exception))

    def test_promotional_price_raise_value_error_new_price_equal_price(self):
        with self.assertRaises(ValueError) as err:
            self.car.set_promotional_price(5000.50)
        self.assertEqual("You are supposed to decrease the price!", str(err.exception))

    def test_promotional_price_return_str_for_successfully_set(self):
        actual = self.car.set_promotional_price(1000)
        self.assertEqual("The promotional price has been successfully set.", actual)

    def test_promotional_price_change_price(self):
        actual = self.car.set_promotional_price(1000)
        self.assertEqual(1000, self.car.price)

    def test_need_repair_is_impossible(self):
        actual = self.car.need_repair(2501, "test")
        self.assertEqual("Repair is impossible!", actual)

    def test_need_repair_return_str_for_repair(self):
        actual = self.car.need_repair(2500, "test")
        self.assertEqual("Price has been increased due to repair charges.", actual)

    def test_need_repair_change_price_car(self):
        self.car.need_repair(2500, "test")
        self.assertEqual(7500.50, self.car.price)

    def test_need_repair_add_description_in_repairs(self):
        self.car.repairs = ["repair1", "repair2"]
        self.car.need_repair(2500, "test")
        self.assertEqual(['repair1', 'repair2', 'test'], self.car.repairs)

    def test__gt__for_different_type(self):
        test_car = SecondHandCar("model", "test_type2", 200, 5000.50)
        actual = self.car.__gt__(test_car)
        self.assertEqual("Cars cannot be compared. Type mismatch!", actual)

    def test__gt__for_equal_type_return_true(self):
        test_car = SecondHandCar("model", "test_type", 200, 1000.50)
        actual = self.car.__gt__(test_car)
        self.assertTrue(actual)

    def test__gt__for_equal_type_return_false(self):
        test_car = SecondHandCar("model", "test_type", 200, 6000.50)
        actual = self.car.__gt__(test_car)
        self.assertFalse(actual)

    def test__str__(self):
        actual = str(self.car)
        self.assertEqual(('Model model | Type test_type | Milage 200km\n'
 'Current price: 5000.50 | Number of Repairs: 0'), actual)



if __name__ == "__main__":
    main()

