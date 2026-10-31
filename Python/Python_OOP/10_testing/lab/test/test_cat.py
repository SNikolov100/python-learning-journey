from unittest import TestCase, main

from lab.projects.cat import Cat


class CatTests(TestCase):

    def setUp(self):
      self.c = Cat("Bingo")

    def test_init(self):
        self.assertEqual("Bingo", self.c.name)
        self.assertFalse(self.c.fed)
        self.assertFalse(self.c.sleepy)
        self.assertEqual(0, self.c.size)

    def test_eat_raise_exception(self):
        self.c.fed = True
        with self.assertRaises(Exception) as ex:
            self.c.eat()
        self.assertEqual("Already fed.", str(ex.exception))
        self.assertEqual(0, self.c.size)

    def test_eat_increased_after_eating(self):
        self.c.eat()
        self.assertEqual(1, self.c.size)
        self.c.fed = False
        self.c.eat()
        self.assertEqual(2, self.c.size)

    def test_eat_fed_after_eating(self):
        self.c.eat()
        self.assertTrue(self.c.fed)

    def test_sleep_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.c.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_sleep_not_sleepy(self):
        self.c.eat()
        self.c.sleep()
        self.assertFalse(self.c.sleepy)



if __name__ == '__main__':
    main()
