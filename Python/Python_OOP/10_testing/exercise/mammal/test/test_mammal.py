from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):

    def setUp(self):
        self.m = Mammal("test_name", "test_type", "test_sound")

    def test_init(self):
        self.assertEqual("test_name", self.m.name)
        self.assertEqual("test_type", self.m.type)
        self.assertEqual("test_sound", self.m.sound)
        self.assertEqual("animals", self.m._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("test_name makes test_sound", self.m.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.m.get_kingdom())

    def test_info(self):
        self.assertEqual("test_name is of type test_type", self.m.info())



if __name__ == "__main__":
    main()