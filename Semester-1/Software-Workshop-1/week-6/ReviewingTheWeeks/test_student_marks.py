from unittest import TestCase
import student_marks

class TestClass(TestCase):

    def test_split_data(self):
        assert student_marks.split_data() == [['Ann Smith', 51, 60, 80], ['Derek Jones', 12, 49, 90], ['Hannah Qui', 55, 90,
                                              85],['Anya Lopez', 55, 60, 75]]
#assert is an aid to debugging - if the condition is true it passes the test

    def test_extract_surname(self):
        student_list = [['Ann Smith', 51, 60, 80, 63], ['Derek Jones', 12, 49, 90, 50], ['Hannah Qui', 55, 90,
                                              85, 76],['Anya Lopez', 55, 60, 75, 63]]
        assert student_marks.extract_surname(student_list) == ['Smith', 'Jones', 'Qui', 'Lopez']
