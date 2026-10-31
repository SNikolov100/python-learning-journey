from project.robot import Robot
from unittest import TestCase, main

class RobotTest(TestCase):
    def setUp(self):
        self.rob = Robot("test_robot", "Military", 10, 10_000.10)

    def test_init_to_default(self):
        self.assertEqual("test_robot", self.rob.robot_id)
        self.assertEqual("Military", self.rob.category)
        self.assertEqual(10, self.rob.available_capacity)
        self.assertEqual(10_000.10, self.rob.price)
        self.assertFalse(self.rob.hardware_upgrades)
        self.assertFalse(self.rob.software_updates)
        self.assertEqual(1.5, self.rob.PRICE_INCREMENT)

    def test_inti_types(self):
        self.assertIsInstance(self.rob.robot_id, str)
        self.assertIsInstance(self.rob.category, str)
        self.assertIsInstance(self.rob.available_capacity, int)
        self.assertIsInstance(self.rob.price, float)
        self.assertIsInstance(self.rob.hardware_upgrades, list)
        self.assertIsInstance(self.rob.software_updates, list)

    def test_category_raise_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.rob.category = "test"
        expected = "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        self.assertEqual(expected, str(err.exception))

    def test_valid_categories(self):
        self.rob.category = "Education"
        self.assertEqual("Education", self.rob.category)
        self.rob.category = "Entertainment"
        self.assertEqual("Entertainment", self.rob.category)
        self.rob.category = "Humanoids"
        self.assertEqual("Humanoids", self.rob.category)

    def test_price_raise_value_error_less_then_zero(self):
        with self.assertRaises(ValueError) as err:
            self.rob.price = -0.34
        self.assertEqual("Price cannot be negative!", str(err.exception))

    def test_upgrade_not_upgraded(self):
        self.rob.hardware_upgrades = ["test1", "test2"]
        actual = self.rob.upgrade("test2", 1000.10)
        self.assertEqual("Robot test_robot was not upgraded.", actual)

    def test_upgrade_upgraded_return_string(self):
        self.rob.hardware_upgrades = ["test1", "test2"]
        actual = self.rob.upgrade("test3", 1000.10)
        self.assertEqual("Robot test_robot was upgraded with test3.", actual)

    def test_upgrade_upgraded_write_in_hardware_upgrades(self):
        self.rob.hardware_upgrades = ["test1", "test2"]
        self.rob.upgrade("test3", 1000.10)
        self.assertEqual(["test1", "test2", "test3"], self.rob.hardware_upgrades)

    def test_upgrade_upgraded_change_price(self):
        self.rob.hardware_upgrades = ["test1", "test2"]
        self.rob.upgrade("test3", 1000.10)
        self.assertEqual(11500.25, self.rob.price)

    def test_update_robot_was_not_updated_has_soft_upd_and_vers_less_then_max_version(self):
        self.rob.software_updates = [1.1, 2, 4.1]
        actual = self.rob.update(3.1, 10)
        self.assertEqual("Robot test_robot was not updated.", actual)

    def test_update_robot_was_not_updated_has_soft_upd_and_vers_equal_max_version(self):
        self.rob.software_updates = [1.1, 2, 4.1]
        actual = self.rob.update(4.1, 11)
        self.assertEqual("Robot test_robot was not updated.", actual)

    def test_update_robot_was_not_updated_capacity_less_then_needed_capacity(self):
        actual = self.rob.update(4.1, 11)
        self.assertEqual("Robot test_robot was not updated.", actual)

    def test_update_robot_return_string_was_updated(self):
        self.rob.software_updates = [1.1, 2, 4.1]
        actual = self.rob.update(4.12, 5)
        self.assertEqual("Robot test_robot was updated to version 4.12.", actual)

    def test_update_robot_add_version_in_software_updates(self):
        self.rob.software_updates = [1.1, 2, 4.1]
        self.rob.update(4.12, 5)
        self.assertEqual([1.1, 2, 4.1, 4.12], self.rob.software_updates)

    def test_update_robot_update_capacity(self):
        self.rob.software_updates = [1.1, 2, 4.1]
        self.rob.update(4.12, 4)
        self.assertEqual(6, self.rob.available_capacity)

    def test__gt__other_is_more_expensive(self):
        rob_test = Robot("rob_test", "Military", 5, 5_000.10)
        actual = self.rob.__gt__(rob_test)
        expected = "Robot with ID test_robot is more expensive than Robot with ID rob_test."
        self.assertEqual(expected, actual)

    def test__gt__equal_price(self):
        rob_test = Robot("rob_test", "Military", 5, 10_000.10)
        actual = self.rob.__gt__(rob_test)
        expected = "Robot with ID test_robot costs equal to Robot with ID rob_test."
        self.assertEqual(expected, actual)

    def test__gt__(self):
        rob_test = Robot("rob_test", "Military", 5, 11_000.10)
        actual = self.rob.__gt__(rob_test)
        expected = "Robot with ID test_robot is cheaper than Robot with ID rob_test."
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    main()