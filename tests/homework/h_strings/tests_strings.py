import unittest 
from src.homework.h_strings.value_return import get_hamming_distance 
from src.homework.h_strings.value_return import get_dna_complement 
 
class Test_Config(unittest.TestCase): 

    def test_get_hamming_distance(self):
           self.assertEqual(get_hamming_distance(GAGCCTACTAACGGGAT, CATCGTAATGACGGCCT), 7)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(AAAACCCGGT), ACCGGGTTTT)