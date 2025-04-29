#

import unittest

from src.homework.j_classes.class_a import die

class TestDie(unittest.TestCase):
    
    def test_die_roll(self):
        d = die()
       
        for _ in range(3):
            d.roll()
            val = d.get_rolled_value()
            self.assertIn(val, range(1, 7), "Roll value out of bounds!")

if __name__ == "__main__":
    unittest.main()
