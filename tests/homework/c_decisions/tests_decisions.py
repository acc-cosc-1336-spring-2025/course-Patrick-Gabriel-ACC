import unittest

from src.homework.c_decisions.decisions import get_options_ratio 
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):
    
    def test_get_options_ratio_5_20(self):
        self.assertEqual(get_options_ratio(5, 20), 0.25)

    def test_get_options_ratio_10_20(self):
        self.assertEqual(get_options_ratio(10, 20), 0.5)


    def test_get_faculty_rating_excellent(self):
        self.assertEqual(get_faculty_rating(0.91), "Excellent")

    def test_get_faculty_rating_very_good(self):
        self.assertEqual(get_faculty_rating(0.85), "Very Good")

    def test_get_faculty_rating_good(self):
        self.assertEqual(get_faculty_rating(0.71), "Good")

    def test_get_faculty_rating_needs_improvement(self):
        self.assertEqual(get_faculty_rating(0.66), "Needs Improvement")

    def test_get_faculty_rating_unacceptable(self):
        self.assertEqual(get_faculty_rating(0.45), "Unacceptable")