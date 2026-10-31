from unittest import TestCase, main

from lab.projects.car_manager import Car


class CarTests(TestCase):

    def setUp(self):
        self.c = Car("a", "b", 1, 4)

    def test_init(self):
        self.assertEqual("a", self.c.make)
        self.assertEqual("b", self.c.model)
        self.assertEqual(1, self.c.fuel_consumption)
        self.assertEqual(4, self.c.fuel_capacity)
        self.assertEqual(0, self.c.fuel_amount)

    # def test_make(self):
    #     with self.assertRaises(Exception) as ex:
    #         self.c.make = ""
    #     self.assertEqual("Make cannot be null or empty!", str(ex.exception))
    #
    #     with self.assertRaises(Exception) as ex:
    #         self.c.make = None
    #     self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    invalid_values = (None, "")
    def test_make_raise_exception_for_null_or_empty(self):
        for el in self.invalid_values:
            with self.subTest(value=el):
                with self.assertRaises(Exception) as ex:
                    self.c.make = el
                self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model(self):
        with self.assertRaises(Exception) as ex:
            self.c.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.c.model = None
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.c.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.c.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

        self.c.fuel_amount = 4
        self.assertEqual(4, self.c.fuel_amount)

    def test_refuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.c.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.c.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_add_fuel(self):
        self.c.refuel(1)
        self.assertEqual(1, self.c.fuel_amount)
        self.c.refuel(1)
        self.assertEqual(2, self.c.fuel_amount)

    def test_refuel_amount_bigger_then_capacity(self):
        self.c.refuel(5)
        self.assertEqual(4, self.c.fuel_amount)

    def test_drive_raise_exception_not_enough_fuel(self):
        self.c.fuel_amount = 4
        with self.assertRaises(Exception) as ex:
            self.c.drive(500)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.assertEqual(4, self.c.fuel_amount)
        self.c.drive(400)
        self.assertEqual(0, self.c.fuel_amount)

    def test_drive_decrease_fuel_amount(self):
        self.c.fuel_amount = 4
        self.c.drive(100)
        self.assertEqual(3, self.c.fuel_amount)
        self.c.drive(100)
        self.assertEqual(2, self.c.fuel_amount)

if __name__ == "__main__":
    main()