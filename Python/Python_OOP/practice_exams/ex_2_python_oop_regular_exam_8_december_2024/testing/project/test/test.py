from project.senior_student import SeniorStudent
from unittest import TestCase, main

class SeniorStudentTest(TestCase):

    def setUp(self):
        self.st = SeniorStudent("12345", "test name", 5.5 )

    def test_init(self):
        self.assertEqual("12345", self.st.student_id)
        self.assertEqual("test name", self.st.name)
        self.assertEqual(5.5, self.st.student_gpa)
        self.assertEqual(set(), self.st.colleges)

    def test_student_id_raise_value_error_id_less_then_4_characters(self):
        with self.assertRaises(ValueError) as err:
            self.st.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!", str(err.exception))

    def test_student_id_raise_value_error_id_has_white_spaces(self):
        with self.assertRaises(ValueError) as err:
            self.st.student_id = "   12"
        self.assertEqual("Student ID must be at least 4 digits long!", str(err.exception))

    def test_name_raise_value_error_name_null(self):
        with self.assertRaises(ValueError) as err:
            self.st.name = ""
        self.assertEqual("Student name cannot be null or empty!", str(err.exception))

    def test_name_raise_value_error_name_empty(self):
        with self.assertRaises(ValueError) as err:
            self.st.name = " " * 5
        self.assertEqual("Student name cannot be null or empty!", str(err.exception))

    def test_student_gpa_raise_value_error_less_then_1(self):
        with self.assertRaises(ValueError) as err:
            self.st.student_gpa = 0.99999
        self.assertEqual("Student GPA must be more than 1.0!", str(err.exception))

    def test_student_gpa_raise_value_error_equal_then_1(self):
        with self.assertRaises(ValueError) as err:
            self.st.student_gpa = 1.0
        self.assertEqual("Student GPA must be more than 1.0!", str(err.exception))

    def test_apply_to_college_application_failed(self):
        self.assertEqual("Application failed!", self.st.apply_to_college(5.6, "test1"))

    def test_apply_to_college_add_application(self):
        self.st.colleges.add("test1")
        actual = self.st.apply_to_college(5.5, "test3")
        self.assertEqual({"test1", "TEST3"}, self.st.colleges)
        self.assertEqual("test name successfully applied to test3.", actual)

    def test_update_gpa_not_been_changed_equal(self):
        actual = self.st.update_gpa(1.0)
        self.assertEqual("The GPA has not been changed!", actual)

    def test_update_gpa_not_been_changed_less_then_1(self):
        actual = self.st.update_gpa(0.9999)
        self.assertEqual("The GPA has not been changed!", actual)

    def test_update_gpa_successfully_updated(self):
        actual = self.st.update_gpa(1.1)
        self.assertEqual(1.1, self.st.student_gpa)
        self.assertEqual("Student GPA was successfully updated.", actual)

    def test_eq_method_true(self):
        self.st2 = SeniorStudent("123456", "test2 name", 5.5)
        self.assertTrue(self.st.__eq__(self.st2))

    def test_eq_method_false(self):
        self.st2 = SeniorStudent("123455", "test2 name", 6.7)
        self.assertFalse(self.st.__eq__(self.st2))


if __name__ == "__main__":
    main()

