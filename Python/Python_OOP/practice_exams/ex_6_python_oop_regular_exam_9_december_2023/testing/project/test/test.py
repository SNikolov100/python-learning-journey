from unittest import TestCase, main

from project.railway_station import RailwayStation
from collections import deque

class RailwayStationTest(TestCase):

    def setUp(self):
        self.rs = RailwayStation("name")

    def test_init_to_default(self):
        self.assertEqual("name", self.rs.name)
        self.assertFalse(self.rs.arrival_trains)
        self.assertFalse(self.rs.departure_trains)

    def test_unit_to_type(self):
        self.assertIsInstance(self.rs.name, str)
        self.assertIsInstance(self.rs.arrival_trains, deque)
        self.assertIsInstance(self.rs.departure_trains, deque)

    def test_name_raise_value_error_less_3_symbols(self):
        with self.assertRaises(ValueError) as err:
            self.rs.name = "te"
        self.assertEqual("Name should be more than 3 symbols!", str(err.exception))

    def test_name_raise_value_error_equal_3_symbols(self):
        with self.assertRaises(ValueError) as err:
            self.rs.name = "tes"
        self.assertEqual("Name should be more than 3 symbols!", str(err.exception))

    def test_new_arrival_on_board_type(self):
        self.rs.new_arrival_on_board("test_arrival")
        self.assertEqual(deque(['test_arrival']), self.rs.arrival_trains)

    def test_new_arrival_on_board_append(self):
        self.rs.new_arrival_on_board("test_arrival")
        self.assertEqual("test_arrival", self.rs.arrival_trains[0])

    def test_new_arrival_on_board_len_on_deque(self):
        self.rs.new_arrival_on_board("test_arrival")
        self.assertEqual(1, len(self.rs.arrival_trains))

    def test_train_has_arrived_other_trains_to_arrive_other_train(self):
        self.rs.arrival_trains = deque(["train1", "train2"])
        actual = self.rs.train_has_arrived("test_arrival")
        self.assertEqual("There are other trains to arrive before test_arrival.", actual)


    def test_train_has_arrived_other_trains_to_arrive_the_same_train(self):
        self.rs.arrival_trains = deque(["train1", "train2"])
        actual = self.rs.train_has_arrived("train1")
        self.assertEqual("train1 is on the platform and will leave in 5 minutes.", actual)

    def test_train_has_left_popleft_to_departure(self):
        self.rs.departure_trains = deque(["train1", "train2"])
        self.rs.train_has_left("train1")
        self.assertEqual(deque(["train2"]), self.rs.departure_trains)

    def test_train_has_left_return_true(self):
        self.rs.departure_trains = deque(["train1", "train2"])
        actual = self.rs.train_has_left("train1")
        self.assertTrue(actual)

    def test_train_has_left_return_false_for_empty_departure_trains(self):
        actual = self.rs.train_has_left("train1")
        self.assertFalse(actual)

    def test_train_has_left_return_false_for_not_equal_train_info(self):
        self.rs.departure_trains = deque(["train1", "train2"])
        actual = self.rs.train_has_left("train2")
        self.assertFalse(actual)






if __name__ == "__main__":
    main()