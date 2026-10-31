from project.gallery import Gallery

from unittest import TestCase, main

class GalleryTest(TestCase):
    def setUp(self):
        self.g = Gallery("name", "city", 20.20)

    def test_init_with_default(self):
        self.assertEqual("name", self.g.gallery_name)
        self.assertEqual("city", self.g.city)
        self.assertEqual(20.20, self.g.area_sq_m)
        self.assertTrue(self.g.open_to_public)
        self.assertDictEqual({}, self.g.exhibitions)

    def test_init_with_not_default(self):
        self.g.open_to_public = False
        self.g.exhibitions = {"test1": 1, "test2": 2}
        self.assertFalse(self.g.open_to_public)
        self.assertDictEqual({"test1": 1, "test2": 2}, self.g.exhibitions)

    def test_name_raise_value_error_not_letters_and_digits(self):
        with self.assertRaises(ValueError) as ex:
            self.g.gallery_name = "_ "
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_name_raise_value_error_empty_space_between_name(self):
        with self.assertRaises(ValueError) as ex:
            self.g.gallery_name = "test 123"
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_name_raise_value_error_empty_spaces(self):
        with self.assertRaises(ValueError) as ex:
            self.g.gallery_name = " " * 10
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_name_raise_value_error_a_empty_space(self):
        with self.assertRaises(ValueError) as ex:
            self.g.gallery_name = ""
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_name_valid_strip(self):
        self.g.gallery_name = " 123 "
        self.assertEqual("123", self.g.gallery_name)

    def test_name_valid(self):
        self.g.gallery_name = "test123"
        self.assertEqual("test123", self.g.gallery_name)

    def test_city_raise_value_error_name_start_with_empty_space(self):
        with self.assertRaises(ValueError) as ex:
            self.g.city = " test"
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_city_raise_value_error_name_start_with_digit(self):
        with self.assertRaises(ValueError) as ex:
            self.g.city = "1test"
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_city_raise_value_error_name_start_with_underscore(self):
        with self.assertRaises(ValueError) as ex:
            self.g.city = "_test"
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_city_raise_value_error_name_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.g.city = ""
        self.assertEqual("City name must start with a letter!", str(ex.exception))


    def test_area_sq_m_raise_value_error_equal_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.g.area_sq_m = 0
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_area_sq_m_raise_value_error_less_then_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.g.area_sq_m = -1
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_add_exhibition_name_already_exist(self):
        self.g.exhibitions = {"test1": 1, "test2": 2}
        self.assertEqual('Exhibition "test2" already exists.', self.g.add_exhibition("test2", 3))

    def test_add_exhibition_name(self):
        self.g.exhibitions = {"test1": 1, "test2": 2}
        actual = self.g.add_exhibition("test3", 3)
        self.assertEqual({"test1":1, "test2":2, "test3": 3}, self.g.exhibitions)
        self.assertEqual('Exhibition "test3" added for the year 3.', actual)

    def test_remove_exhibition_name_is_not_exist(self):
        self.g.exhibitions = {"test1": 1, "test2": 2}
        self.assertEqual('Exhibition "test3" not found.', self.g.remove_exhibition("test3"))

    def test_remove_exhibition_name_is(self):
        self.g.exhibitions = {"test1": 1, "test2": 2}
        actual = self.g.remove_exhibition("test1")
        self.assertEqual({"test2": 2}, self.g.exhibitions)
        self.assertEqual('Exhibition "test1" removed.', actual)


    def test_list_exhibitions_return_items_open_to_public_is_true(self):
        self.g.exhibitions = {"test1": 1, "test2": 2}
        self.assertEqual("test1: 1\ntest2: 2", self.g.list_exhibitions())

    def test_list_exhibitions_return_items_open_to_public_is_false(self):
        self.g.open_to_public = False
        self.assertEqual('Gallery name is currently closed for public! Check for updates later on.', self.g.list_exhibitions())



if __name__ == "__main__":
    main()
