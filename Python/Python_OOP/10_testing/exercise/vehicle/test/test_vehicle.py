from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):

    def setUp(self):
        self.c = Vehicle(50.00, 100.00)

    def test_class_parameters(self):
        self.assertEqual(1.25, self.c.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(Vehicle.__annotations__["fuel_consumption"], float)
        self.assertEqual(Vehicle.__annotations__["fuel"], float)
        self.assertEqual(Vehicle.__annotations__["capacity"], float)
        self.assertEqual(Vehicle.__annotations__["horse_power"], float)

    def test_init(self):
        self.assertEqual(50.00, self.c.fuel)
        self.assertEqual(50.00, self.c.capacity)
        self.assertEqual(100.00, self.c.horse_power)
        self.assertEqual(1.25, self.c.fuel_consumption)

    def test_drive_raise_exception_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.c.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(50.00, self.c.fuel)

    def test_drive_with_enough_fuel(self):
        self.c.drive(10)
        self.assertEqual(37.50, self.c.fuel)

    def test_refuel_raise_exception_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.c.refuel(51)
        self.assertEqual("Too much fuel", str(ex.exception))
        self.assertEqual(50.00, self.c.fuel)


    def test_refuel_under_capacity(self):
        self.c.fuel = 10
        self.c.refuel(20)
        self.assertEqual(30, self.c.fuel)

    def test_str(self):
        assert_result = f"The vehicle has 100.0 horse power with 50.0 fuel left and 1.25 fuel consumption"
        self.assertEqual(assert_result, self.c.__str__)

if __name__ == "__main__":
    main()