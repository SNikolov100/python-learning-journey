from unittest import TestCase, main

from project.trip import Trip

class TripTest(TestCase):

    def setUp(self):
        self.trip = Trip(2500.5, 5, True)

    def test_init_to_default(self):
        self.assertEqual(2500.5, self.trip.budget)
        self.assertEqual(5, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertFalse(self.trip.booked_destinations_paid_amounts)

    def test_init_to_type(self):
        self.assertIsInstance(self.trip.budget, float)
        self.assertIsInstance(self.trip.travelers, int)
        self.assertIsInstance(self.trip.is_family, bool)
        self.assertIsInstance(self.trip.booked_destinations_paid_amounts, dict)

    def test_travelers_raise_value_error_less_then_one_person(self):
        with self.assertRaises(ValueError) as err:
            self.trip.travelers = 0
        self.assertEqual("At least one traveler is required!", str(err.exception))

    def test_is_family_entered_value_false(self):
        self.trip.is_family = False
        self.assertFalse(self.trip.is_family)

    def test_is_family_entered_value_true_and_travels_less_then_two(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertFalse(self.trip.is_family)

    def test_is_family_entered_value_true_and_travels_more_then_two(self):
        self.trip.is_family = True
        self.trip.travelers = 2
        self.assertTrue(self.trip.is_family)

    def test_book_a_trip_not_property_destination(self):
        expected = "This destination is not in our offers, please choose a new one!"
        self.assertEqual(expected, self.trip.book_a_trip("New Zealand1"))

    def test_book_a_trip_has_family_true_and_budget_is_not_enough(self):
        self.trip.budget = 2249.99
        actual = self.trip.book_a_trip("Bulgaria")
        self.assertEqual("Your budget is not enough!", actual)

    def test_book_a_trip_has_not_family_true_and_budget_is_not_enough(self):
        self.trip.budget = 499.99
        actual = self.trip.book_a_trip("Bulgaria")
        self.assertEqual("Your budget is not enough!", actual)

    def test_book_a_trip_has_family_true_successfully_booked(self):
        actual = self.trip.book_a_trip("Bulgaria")
        expected = "Successfully booked destination Bulgaria! Your budget left is 250.50"
        self.assertEqual(expected, actual)

    def test_book_a_trip_has_family_true_successfully_booked_write_in_book_destination(self):
        self.trip.booked_destinations_paid_amounts = {"Bulgaria": 500}
        self.trip.book_a_trip("Bulgaria")
        self.assertEqual({"Bulgaria": 2250.0}, self.trip.booked_destinations_paid_amounts)

    def test_booking_status_no_booking_yet(self):
        actual = self.trip.booking_status()
        self.assertEqual("No bookings yet. Budget: 2500.50", actual)

    def test_booking_status_result(self):
        self.trip.booked_destinations_paid_amounts = {"Bulgaria": 2250, 'Australia': 5700}
        actual = self.trip.booking_status()
        expected = ('Booked Destination: Australia\n'
 'Paid Amount: 5700.00\n'
 'Booked Destination: Bulgaria\n'
 'Paid Amount: 2250.00\n'
 'Number of Travelers: 5\n'
 'Budget Left: 2500.50')
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    main()
