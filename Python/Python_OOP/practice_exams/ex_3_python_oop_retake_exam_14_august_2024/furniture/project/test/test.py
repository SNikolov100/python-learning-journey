from unittest import TestCase, main

from project.furniture import Furniture

class FurnitureTest(TestCase):

    def setUp(self):
        self.table = Furniture("test1", 20.50, (2,2,2))

    def test_init_with_default_arguments(self):
        self.assertEqual("test1", self.table.model)
        self.assertEqual(20.50, self.table.price)
        self.assertEqual((2, 2, 2), self.table.dimensions)
        self.assertTrue(self.table.in_stock)
        self.assertIsNone(self.table.weight)

    def test_init_with_arguments(self):
        self.table.in_stock = False
        self.table.weight = 5.55
        self.assertFalse(self.table.in_stock)
        self.assertEqual(5.55, self.table.weight)

    def test_model_raise_value_error_empty_string(self):
        with self.assertRaises(ValueError) as err:
            self.table.model = ""
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(err.exception))

    def test_model_raise_value_error_with_white_spaces(self):
        with self.assertRaises(ValueError) as err:
            self.table.model = " " * 3
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(err.exception))

    def test_model_raise_value_error_more_then_50_length(self):
        with self.assertRaises(ValueError) as err:
            self.table.model = "f" * 51
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(err.exception))

    def test_price_raise_value_error_negative_price(self):
        with self.assertRaises(ValueError) as err:
            self.table.price = -0.1
        self.assertEqual("Price must be a non-negative number.", str(err.exception))

    def test_dimensions_raise_value_error_contain_2_integers(self):
        with self.assertRaises(ValueError) as err:
            self.table.dimensions = (2, 2)
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(err.exception))

    def test_dimensions_raise_value_error_contain_4_integers(self):
        with self.assertRaises(ValueError) as err:
            self.table.dimensions = (4, 4, 4, 4)
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(err.exception))

    def test_dimensions_raise_value_error_greater_then_zero(self):
        with self.assertRaises(ValueError) as err:
            self.table.dimensions = ( 0, -1, 0)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(err.exception))

    def test_weight_raise_value_error_weight_equal_to_zero(self):
        with self.assertRaises(ValueError) as err:
            self.table.weight = 0.0
        self.assertEqual("Weight must be greater than zero.", str(err.exception))

    def test_weight_raise_value_error_weight_under_to_zero(self):
        with self.assertRaises(ValueError) as err:
            self.table.weight = -1.0
        self.assertEqual("Weight must be greater than zero.", str(err.exception))

    def test_weight_is_none(self):
        self.assertIsNone(self.table.weight)

    def test_get_available_status_in_stock(self):
        actual = self.table.get_available_status()
        self.assertEqual(f"Model: test1 is currently in stock.", actual)

    def test_get_available_status_unavailable(self):
        self.table.in_stock = False
        actual = self.table.get_available_status()
        self.assertEqual(f"Model: test1 is currently unavailable.", actual)

    def test_get_specifications_with_not_available(self):
        actual = self.table.get_specifications()
        self.assertEqual("Model: test1 has the following dimensions: 2mm x 2mm x 2mm and weighs: N/A", actual)

    def test_get_specifications_with_weight(self):
        self.table.weight = 4.5
        actual = self.table.get_specifications()
        self.assertEqual("Model: test1 has the following dimensions: 2mm x 2mm x 2mm and weighs: 4.5", actual)



if __name__ == "__main__":
    main()

