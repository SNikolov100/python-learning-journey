from unittest import TestCase, main

from project.truck_driver import TruckDriver

class TruckDriverTest(TestCase):

    def setUp(self):
        self.td = TruckDriver("test_name1",10.5 )

    def test_init_to_default(self):
        self.assertEqual("test_name1", self.td.name)
        self.assertEqual(10.5, self.td.money_per_mile)
        self.assertFalse(self.td.available_cargos)
        self.assertEqual(0, self.td.earned_money)
        self.assertEqual(0, self.td.miles)

    def test_init_types(self):
        self.td.earned_money = 100.10
        self.assertIsInstance(self.td.name, str)
        self.assertIsInstance(self.td.money_per_mile, float)
        self.assertIsInstance(self.td.available_cargos, dict)
        self.assertIsInstance(self.td.earned_money, float)
        self.assertIsInstance(self.td.miles, int)

    def test_available_cargos_for_key_and_value(self):
        self.td.available_cargos = {"test2": 10}
        for key, value in self.td.available_cargos.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, int)

    def test_earned_money_raise_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.td.earned_money = -0.5
        self.assertEqual("test_name1 went bankrupt.", str(err.exception))

    def test_add_cargo_offer_raise_exception(self):
        self.td.available_cargos = {"point1": 10, "point2": 20}
        with self.assertRaises(Exception) as err:
            self.td.add_cargo_offer("point1", 20)
        self.assertEqual("Cargo offer is already added.", str(err.exception))

    def test_add_cargo_offer_return_string(self):
        self.td.available_cargos = {"point1": 10, "point2": 20}
        actual = self.td.add_cargo_offer("point3", 20)
        expected = "Cargo for 20 to point3 was added as an offer."
        self.assertEqual(expected, actual)

    def test_add_cargo_offer_write_in_available_cargos(self):
        self.td.available_cargos = {"point1": 10, "point2": 20}
        self.td.add_cargo_offer("point3", 20)
        self.assertEqual({"point1": 10, "point2": 20, "point3": 20}, self.td.available_cargos)

    def test_bankrupt_drive_cargo(self):
        self.td.money_per_mile = 1
        self.td.available_cargos = {"point1": 10, "point2": 20_000}
        with self.assertRaises(ValueError) as err:
            self.td.drive_best_cargo_offer()
        self.assertEqual("test_name1 went bankrupt.", str(err.exception))


    def test_drive_best_cargo_offer_raise_value_error(self):
        actual = self.td.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", actual)

    def test_drive_best_cargo_return_string(self):
        self.td.available_cargos = {"point1": 10, "point2": 20}
        actual = self.td.drive_best_cargo_offer()
        self.assertEqual("test_name1 is driving 20 to point2.", actual)

    def test_drive_best_cargo_check_money(self):
        self.td.earned_money = 0
        self.td.available_cargos = {"point1": 10, "point2": 2000}
        self.td.money_per_mile = 1
        self.td.drive_best_cargo_offer()
        self.assertEqual(1250, self.td.earned_money)

    def test_drive_best_cargo_take_max_miles(self):
        self.td.available_cargos = {"point1": 10, "point2": 2000}
        actual = self.td.drive_best_cargo_offer()
        self.assertIn("point2", actual)
        self.assertIn("2000", actual)


    def test_drive_best_cargo_check_miles(self):
        self.td.available_cargos = {"point1": 10, "point2": 20}
        self.td.drive_best_cargo_offer()
        self.assertEqual(20, self.td.miles)

    def test_check_for_activities(self):
        self.td.earned_money = 1500
        self.td.check_for_activities(250)
        self.assertEqual(1480, self.td.earned_money)

    def test_check_for_activities_no_events(self):
        self.td.earned_money = 1500
        self.td.check_for_activities(50)
        self.assertEqual(1500, self.td.earned_money)

    def test_eat_not_multiple(self):
        self.td.earned_money = 1500
        self.td.eat(30)
        self.assertEqual(1500, self.td.earned_money)

    def test_eat_is_multiple(self):
        self.td.earned_money = 1500
        self.td.eat(250)
        self.assertEqual(1480, self.td.earned_money)

    def test_sleep_not_multiple(self):
        self.td.earned_money = 10000
        self.td.sleep(300)
        self.assertEqual(10000, self.td.earned_money)

    def test_sleep_with_multiple(self):
        self.td.earned_money = 10000
        self.td.sleep(1000)
        self.assertEqual(9955, self.td.earned_money)

    def test_pump_gas_not_multiple(self):
        self.td.earned_money = 10000
        self.td.pump_gas(300)
        self.assertEqual(10000, self.td.earned_money)

    def test_pump_gas_is_multiple(self):
        self.td.earned_money = 10000
        self.td.pump_gas(1500)
        self.assertEqual(9500, self.td.earned_money)

    def test_repair_truck_is_multiple(self):
        self.td.earned_money = 100_000
        self.td.repair_truck(20_000)
        self.assertEqual(92_500, self.td.earned_money)

    def test_repair_truck_not_multiple(self):
        self.td.earned_money = 100_000
        self.td.repair_truck(23_000)
        self.assertEqual(100_000, self.td.earned_money)

    def test_repr(self):
        self.td.miles = 100
        actual = self.td.__repr__()
        self.assertEqual("test_name1 has 100 miles behind his back.", actual)


if __name__ == "__main__":
    main()