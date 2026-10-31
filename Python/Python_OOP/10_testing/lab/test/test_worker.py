from unittest import TestCase, main
from lab.projects.worker import Worker


class WorkerTests(TestCase):
    def test_init(self):
        w = Worker("Ivan", 200, 100)
        self.assertEqual("Ivan", w.name)
        self.assertEqual(200, w.salary)
        self.assertEqual(100, w.energy)
        self.assertEqual(0, w.money)

    def test_work_energy_raise_exception(self):
        w = Worker("Ivan", 200, 0)
        with self.assertRaises(Exception) as ex:
            w.work()
        self.assertEqual("Not enough energy.", str(ex.exception))
        w.energy = -1
        with self.assertRaises(Exception) as ex:
            w.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_add_salary(self):
        w = Worker("Ivan", 200, 100)
        w.work()
        self.assertEqual(200, w.money)
        w.work()
        self.assertEqual(400, w.money)

    def test_work_add_energy(self):
        w = Worker("Ivan", 200, 100)
        w.work()
        self.assertEqual(99, w.energy)
        w.work()
        self.assertEqual(98, w.energy)

    def test_rest(self):
        w = Worker("Ivan", 200, 100)
        w.rest()
        self.assertEqual(101, w.energy)
        w.rest()
        self.assertEqual(102, w.energy)

    def test_get_info(self):
        w = Worker("Ivan", 200, 100)
        w.money = 2000
        self.assertEqual("Ivan has saved 2000 money.", w.get_info())




if __name__ == '__main__':
    main()