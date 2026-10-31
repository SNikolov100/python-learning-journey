import unittest
from unittest import TestCase, main

from project.star_system import StarSystem

class StarSystemTest(TestCase):
    def setUp(self):
        self.ss = StarSystem("test_name1", "Blue giant", "Single", 5)

    def test_unit_to_default(self):
        self.assertEqual("test_name1", self.ss.name)
        self.assertEqual("Blue giant", self.ss.star_type)
        self.assertEqual("Single", self.ss.system_type)
        self.assertEqual(5, self.ss.num_planets)
        self.assertFalse(self.ss.habitable_zone_range)

    def test_init_types(self):
        self.assertIsInstance(self.ss.name, str)
        self.assertIsInstance(self.ss.star_type, str)
        self.assertIsInstance(self.ss.system_type, str)
        self.assertIsInstance(self.ss.num_planets, int)
        self.assertTrue(self.ss.habitable_zone_range is None or isinstance(self.ss.habitable_zone_range, tuple))

    def test_star_types_valid(self):
        self.ss.star_type = "Red giant"
        self.assertEqual("Red giant", self.ss.star_type)
        self.ss.star_type = "Blue giant"
        self.assertEqual("Blue giant", self.ss.star_type)
        self.ss.star_type = "Yellow dwarf"
        self.assertEqual("Yellow dwarf", self.ss.star_type)
        self.ss.star_type = "Red dwarf"
        self.assertEqual("Red dwarf", self.ss.star_type)
        self.ss.star_type = "Brown dwarf"
        self.assertEqual("Brown dwarf", self.ss.star_type)

    def test_star_system_valid(self):
        self.ss.system_type = "Single"
        self.assertEqual("Single", self.ss.system_type)
        self.ss.system_type = "Binary"
        self.assertEqual("Binary", self.ss.system_type)
        self.ss.system_type = "Triple"
        self.assertEqual("Triple", self.ss.system_type)
        self.ss.system_type = "Multiple"
        self.assertEqual("Multiple", self.ss.system_type)

    def test_is_habitable_is_not_habitated_zone_is_none_num_planet_has(self):
        self.assertFalse(self.ss.is_habitable)

    def test_is_habitable_has_habitated_zone_and_num_planet_0(self):
        self.ss = StarSystem("test_name1", "Blue giant", "Single", 0, (1, 3))
        self.assertFalse(self.ss.is_habitable)

    def test_is_habitable_is_true(self):
        self.ss.habitable_zone_range = (1, 2)
        self.assertTrue(self.ss.is_habitable)

    def test_name_raise_value_error_with_empty_string(self):
        with self.assertRaises(ValueError) as err:
            self.ss.name = ""
        self.assertEqual("Name must be a non-empty string.", str(err.exception))

    def test_name_raise_value_error_with_white_spaces(self):
        with self.assertRaises(ValueError) as err:
            self.ss.name = "    "
        self.assertEqual("Name must be a non-empty string.", str(err.exception))

    def test_star_type_raise_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.ss.star_type = "test"
        expected = "Star type must be one of ['Blue giant', 'Brown dwarf', 'Red dwarf', 'Red giant', 'Yellow dwarf']."
        self.assertEqual(expected, str(err.exception))

    def test_system_type_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.ss.system_type = "test"
        expected = "System type must be one of ['Binary', 'Multiple', 'Single', 'Triple']."
        self.assertEqual(expected, str(err.exception))

    def test_num_planets_raise_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.ss.num_planets = -1
        self.assertEqual("Number of planets must be a non-negative integer.", str(err.exception))

    def test_habitable_zone_range_raise_value_error_one_range(self):
        with self.assertRaises(ValueError) as err:
            self.ss.habitable_zone_range = ("1")
        expected = "Habitable zone range must be a tuple of two numbers (start, end) where start < end."
        self.assertEqual(expected, str(err.exception))

    def test_habitable_zone_range_raise_value_error_three_range(self):
        with self.assertRaises(ValueError) as err:
            self.ss.habitable_zone_range = ("1", "test", "ok")
        expected = "Habitable zone range must be a tuple of two numbers (start, end) where start < end."
        self.assertEqual(expected, str(err.exception))

    def test_habitable_zone_range_raise_value_first_element_greater_then_second(self):
        with self.assertRaises(ValueError) as err:
            self.ss.habitable_zone_range = (3, 2)
        expected = "Habitable zone range must be a tuple of two numbers (start, end) where start < end."
        self.assertEqual(expected, str(err.exception))

    def test_habitable_zone_range_raise_value_first_element_equal_second(self):
        with self.assertRaises(ValueError) as err:
            self.ss.habitable_zone_range = (2, 2)
        expected = "Habitable zone range must be a tuple of two numbers (start, end) where start < end."
        self.assertEqual(expected, str(err.exception))

    def test__gt__raise_value_error_both_non_habit(self):
        ss_test = StarSystem("test_name2", "Yellow dwarf", "Binary", 10)
        with self.assertRaises(ValueError) as err:
            self.ss.__gt__(ss_test)
        expected = "Comparison not possible: One or both systems lack a defined habitable zone or planets."
        self.assertEqual(expected, str(err.exception))

    def test__gt__raise_value_error_first_not_habit(self):
        ss_test = StarSystem("test_name2", "Yellow dwarf", "Binary", 10)
        ss_test.habitable_zone_range = (1, 2)
        with self.assertRaises(ValueError) as err:
            self.ss.__gt__(ss_test)
        expected = "Comparison not possible: One or both systems lack a defined habitable zone or planets."
        self.assertEqual(expected, str(err.exception))

    def test__gt__raise_value_error_second_is_not_habit(self):
        ss_test = StarSystem("test_name2", "Yellow dwarf", "Binary", 10)
        self.ss.habitable_zone_range = (1, 2)
        with self.assertRaises(ValueError) as err:
            self.ss.__gt__(ss_test)
        expected = "Comparison not possible: One or both systems lack a defined habitable zone or planets."
        self.assertEqual(expected, str(err.exception))

    def test__gt__return_statement_true(self):
        ss_test = StarSystem("test_name2", "Yellow dwarf", "Binary", 10)
        self.ss.habitable_zone_range = (1, 7)
        ss_test.habitable_zone_range = (1, 6)
        self.assertTrue(self.ss.__gt__(ss_test))

    def test__gt__return_statement_false(self):
        ss_test = StarSystem("test_name2", "Yellow dwarf", "Binary", 10)
        self.ss.habitable_zone_range = (1, 5)
        ss_test.habitable_zone_range = (1, 6)
        self.assertFalse(self.ss.__gt__(ss_test))

    def test_compare_star_systems_first_greater_then_second(self):
        ss_test = StarSystem("test_name2", "Yellow dwarf", "Binary", 10)
        self.ss.habitable_zone_range = (1, 7)
        ss_test.habitable_zone_range = (1, 6)
        actual = StarSystem.compare_star_systems(self.ss, ss_test)
        expected = "test_name1 has a wider habitable zone than test_name2."
        self.assertEqual(expected, actual)

    def test_compare_star_systems_second_greater_then_first(self):
        ss_test = StarSystem("test_name2", "Yellow dwarf", "Binary", 10)
        self.ss.habitable_zone_range = (1, 5)
        ss_test.habitable_zone_range = (1, 6)
        actual = StarSystem.compare_star_systems(self.ss, ss_test)
        expected = "test_name2 has a wider or equal habitable zone compared to test_name1."
        self.assertEqual(expected, actual)

    def test_compare_star_system_raise_value_error(self):
        ss_test = StarSystem("test_name2", "Yellow dwarf", "Binary", 10)
        self.ss.habitable_zone_range = (1, 5)
        actual = StarSystem.compare_star_systems(self.ss, ss_test)
        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.", actual)




if __name__ == "__main__":
    main()