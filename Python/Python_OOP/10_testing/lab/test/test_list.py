
from unittest import TestCase, main

from lab.projects.list import IntegerList


class IntegerListTests(TestCase):

    def setUp(self):
        self.obj = IntegerList(1, 2, 3, 4, "t", "6", 7.3)

    def test_init(self):
        self.assertEqual([1, 2, 3, 4], self.obj.get_data())
        self.assertEqual([1, 2, 3, 4], self.obj._IntegerList__data)

    def test_add(self):
        with self.assertRaises(ValueError) as ex:
            self.obj.add(6.7)
        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.obj.add([])
        self.assertEqual("Element is not Integer", str(ex.exception))

        result = self.obj.add(10)
        self.assertEqual([1, 2, 3, 4, 10], self.obj.get_data())
        self.assertEqual([1, 2, 3, 4, 10], result)

    def test_remove_index(self):
        with self.assertRaises(IndexError) as ex:
            self.obj.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

        result = self.obj.remove_index(0)
        self.assertEqual([2, 3, 4], self.obj.get_data())
        self.assertEqual(1, result)

    def test_insert(self):
        with self.assertRaises(IndexError) as ex:
            self.obj.insert(4, 10)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.obj.insert(0, [])
        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.obj.insert(0, 4.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.obj.insert(0, "45")
        self.assertEqual("Element is not Integer", str(ex.exception))

        self.obj.insert(0, 10)
        self.assertEqual([10, 1, 2, 3, 4], self.obj.get_data())

    def test_get_biggest(self):
        self.assertEqual(4, self.obj.get_biggest())

    def test_get_index(self):
        self.assertEqual(0, self.obj.get_index(1))

    def test_get_element_raise_index_error(self):
        with self.assertRaises(IndexError) as err:
            self.obj.get(10)
        self.assertEqual("Index is out of range", str(err.exception))

    def test_get_element(self):
        self.assertEqual(2, self.obj.get(1))


if __name__ == "__main__":
    main()