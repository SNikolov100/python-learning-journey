from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class ClimbingRobotTest(TestCase):

    def setUp(self):
        self.cr = ClimbingRobot("Alpine", "part_test", 30, 20)

    def test_init_to_default(self):
        self.assertEqual("Alpine", self.cr.category)
        self.assertEqual("part_test", self.cr.part_type)
        self.assertEqual(30, self.cr.capacity)
        self.assertEqual(20, self.cr.memory)
        self.assertFalse(self.cr.installed_software)

    def test_init_instance(self):
        self.assertIsInstance(self.cr.capacity, int)
        self.assertIsInstance(self.cr.memory, int)
        self.assertIsInstance(self.cr.category, str)
        self.assertIsInstance(self.cr.part_type, str)

    def test_category_raise_value_error_for_different_data(self):
        with self.assertRaises(ValueError) as err:
            self.cr.category = "Mountain1"
        self.assertEqual("Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']", str(err.exception))

    def test_category_inti_for_allowed_categories(self):
        my_items = ('Mountain', 'Alpine', 'Indoor', 'Bouldering')
        for item in my_items:
            self.cr.category = item
            self.assertEqual(f"{item}", self.cr.category)

    def test_get_used_capacity(self):
        self.cr.installed_software = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14}
                                    ]
        self.assertEqual(16, self.cr.get_used_capacity())

    def test_get_available_capacity(self):
        self.cr.installed_software = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14}
                                      ]
        actual = self.cr.get_available_capacity()
        self.assertEqual(14, actual)

    def test_get_used_memory(self):
        self.cr.installed_software = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14}
                                      ]
        self.assertEqual(14, self.cr.get_used_memory())

    def test_get_available_memory(self):
        self.cr.installed_software = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14}
                                      ]
        self.assertEqual(6, self.cr.get_available_memory())

    def test_install_software_cannot_install_software_new_software_capacity_memory_are_greater(self):
        self.cr.installed_software = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14}
                                        ]
        soft = {"capacity_consumption": 20,
                "memory_consumption": 20,
                "name": 100}
        actual = self.cr.install_software(soft)
        self.assertEqual("Software '100' cannot be installed on Alpine part.", actual)

    def test_install_software_cannot_install_software_new_software_capacity_is_less_memory_is_greater(self):
        self.cr.installed_software = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14}
                                        ]
        soft = {"capacity_consumption": 2,
                "memory_consumption": 20,
                "name": 100}
        actual = self.cr.install_software(soft)
        self.assertEqual("Software '100' cannot be installed on Alpine part.", actual)

    def test_install_software_cannot_install_software_new_software_capacity_is_greater_memory_is_less(self):
        self.cr.installed_software = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14}
                                      ]
        soft = {"capacity_consumption": 20,
                "memory_consumption": 2,
                "name": 100}
        actual = self.cr.install_software(soft)
        self.assertEqual("Software '100' cannot be installed on Alpine part.", actual)


    def test_install_software_successfully_equal_capacity_and_consumption(self):
        self.cr.installed_software = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14}
                                        ]
        soft = {"capacity_consumption": 14,
                "memory_consumption": 6,
                "name": 100}
        actual = self.cr.install_software(soft)
        expected = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14},
                                        {"capacity_consumption": 14,
                                         "memory_consumption": 6,
                                         "name": 100}
                                        ]
        self.assertEqual(expected, self.cr.installed_software)
        self.assertEqual("Software '100' successfully installed on Alpine part.", actual)


    def test_install_software_successfully_greater_capacity_and_consumption(self):
        self.cr.installed_software = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14}
                                        ]
        soft = {"capacity_consumption": 13,
                "memory_consumption": 5,
                "name": 100}
        actual = self.cr.install_software(soft)
        expected = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14},
                                        {"capacity_consumption": 13,
                                         "memory_consumption": 5,
                                         "name": 100}
                                        ]
        self.assertEqual(expected, self.cr.installed_software)
        self.assertEqual("Software '100' successfully installed on Alpine part.", actual)

    def test_install_software_successfully_greater_capacity_equal_consumption(self):
        self.cr.installed_software = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14}
                                        ]
        soft = {"capacity_consumption": 13,
                "memory_consumption": 6,
                "name": 100}
        actual = self.cr.install_software(soft)
        expected = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14},
                                        {"capacity_consumption": 13,
                                         "memory_consumption": 6,
                                         "name": 100}
                                        ]
        self.assertEqual(expected, self.cr.installed_software)
        self.assertEqual("Software '100' successfully installed on Alpine part.", actual)

    def test_install_software_successfully_equal_capacity_greater_consumption(self):
        self.cr.installed_software = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14}
                                        ]
        soft = {"capacity_consumption": 14,
                "memory_consumption": 5,
                "name": 100}
        actual = self.cr.install_software(soft)
        expected = [{"capacity_consumption": 3,
                                       "memory_consumption": 2,
                                       "name": 4},
                                      {"capacity_consumption": 13,
                                       "memory_consumption": 12,
                                       "name": 14},
                                        {"capacity_consumption": 14,
                                         "memory_consumption": 5,
                                         "name": 100}
                                        ]
        self.assertEqual(expected, self.cr.installed_software)
        self.assertEqual("Software '100' successfully installed on Alpine part.", actual)




    def test_install_software_successfully_empty_installed_software(self):
        soft = {"capacity_consumption": 13,
                "memory_consumption": 5,
                "name": 100}
        actual = self.cr.install_software(soft)
        expected = [{"capacity_consumption": 13, "memory_consumption": 5,"name": 100}]
        self.assertEqual(expected, self.cr.installed_software)
        self.assertEqual("Software '100' successfully installed on Alpine part.", actual)


if __name__ == "__main__":
    main()