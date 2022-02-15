import unittest
import unittest

import unittest
import main

class TestMain(unittest.TestCase):
    def test_calculate_one(self):
        test_param = 10
        result = main.calculate(test_param)
        self.assertEqual(result, 15)

    def test_calculate_two(self):
        test_param = 'abc'
        result = main.calculate(test_param)
        self.assertIsInstance(result, ValueError)

    def test_calculate_three(self):
        test_param = None
        result = main.calculate(test_param)
        self.assertEqual(result, 'please enter number')  

    def test_calculate_three(self):
        test_param = ''
        result = main.calculate(test_param)
        self.assertEqual(result, 'please enter number')        

unittest.main()
