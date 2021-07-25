import unittest
from generators.fibonacci import gen_fibonacci_num


class TestFibonacciNumGenerator(unittest.TestCase):

    def test_result(self):
        fibo_gen = gen_fibonacci_num()
        expected_result = [0, 1, 1, 2, 3, 5, 8, 13]
        actual_result = [next(fibo_gen) for _ in range(8)]
        self.assertEqual(actual_result, expected_result)
