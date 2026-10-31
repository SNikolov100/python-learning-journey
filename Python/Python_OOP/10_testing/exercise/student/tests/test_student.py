from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):

    def setUp(self):
        self.s = Student("name", courses={"test1": ["n1", "n2"],
                                          "test2": ["n11", "n12", "n13"]})

    def test_init(self):
        self.assertEqual("name", self.s.name)
        self.assertEqual({"test1": ["n1", "n2"],
                                "test2": ["n11", "n12", "n13"]
                                }, self.s.courses)

        self.s1 = Student("name1")
        self.assertEqual({}, self.s1.courses)

    def test_enroll_course_name_in_courses(self):
        result = self.s.enroll("test1", ["n3", "n4", "n5"], "n6")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"test1": ["n1", "n2", "n3", "n4", "n5"],
                          "test2": ["n11", "n12", "n13"]}, self.s.courses)

    def test_enroll_course_notes_is_y_string(self):
        result = self.s.enroll("test3", ["n3", "n4", "n5"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"test1": ["n1", "n2"],
                                "test2": ["n11", "n12", "n13"],
                                "test3": ["n3", "n4", "n5"]
                                }, self.s.courses)

    def test_enroll_course_notes_is_empty_string(self):
        result = self.s.enroll("test3", ["n3", "n4", "n5"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"test1": ["n1", "n2"],
                          "test2": ["n11", "n12", "n13"],
                          "test3": ["n3", "n4", "n5"]
                          }, self.s.courses)

    def test_enroll_add_empty_notes(self):
        result = self.s.enroll("test3", ["n3", "n4", "n5"], "N")
        self.assertEqual({"test1": ["n1", "n2"],
                          "test2": ["n11", "n12", "n13"],
                          "test3": []
                          }, self.s.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_if_course_name_in_courses(self):
        self.assertEqual("Notes have been updated", self.s.add_notes("test1", "n3"))
        self.assertEqual({"test1": ["n1", "n2", "n3"],
                                          "test2": ["n11", "n12", "n13"]}, self.s.courses)

    def test_add_notes_raise_exception_cannot_add_notes(self):
        with self.assertRaises(Exception) as ex:
            result = self.s.add_notes("test3", "n3")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_has_it(self):
        result = self.s.leave_course("test1")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({"test2": ["n11", "n12", "n13"]}, self.s.courses)

    def test_leave_course_not_exist_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.s.leave_course("test3")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))




if __name__ == "__main__":
    main()