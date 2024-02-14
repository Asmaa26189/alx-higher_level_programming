#!/usr/bin/python3
import unittest
import sys

# append a new directory to sys.path
sys.path.append('D:\\ALX\\alx-higher_level_programming\\test_pythonAlmostCircle')

# print the updated sys.path
print('Updated sys.path:', sys.path)

from models.base import Base


# class Testbase(unittest.TestCase):
#     """Unittests for testing instantiation of the Base class."""
#     def test_no_arg(self):
#         b1 = Base()
#         b2 = Base()
#         self.assertEqual(b1.id, b2.id - 1)

#     def test_three_args(self):
#         b1 = Base()
#         b2 = Base()
#         b3 = Base()
#         self.assertEqual(b1.id, b3.id - 2)
#     def test_Attribute_Error(self):
#         with self.assertRaises(AttributeError):
#             b = Base(12)
#             print(b.name)
#     def test_TypeError(self):
#         with self.assertRaises(TypeError):
#             Base(1, 2)

class TestBase_save_to_file(unittest.TestCase):
    """TestBase_save_to_file"""

    @classmethod
    def tearDown(self):
        """tearDown"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass
    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

if __name__ == "__main__":
    unittest.main()
