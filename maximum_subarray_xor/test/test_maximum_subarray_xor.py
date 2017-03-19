import unittest
from app.maximum_subarray_xor import maximum_subarray_xor
from nose_parameterized import parameterized

class TestMaximumSubarrayXor(unittest.TestCase):
    @parameterized.expand([
        [[1, 2, 3, 4], [3, 4], 7],
        [[8, 1, 2, 12, 7, 6], [1, 2, 12], 15],
        [[4, 6], [6], 6],
        [[3, 1], [3], 3],
        [[], [], 0]
    ])
    def test_maximum_subarray_xor(self, array, expected_subarray, expected_value):
        subarray, value = maximum_subarray_xor(array)
        self.assertEqual(subarray, expected_subarray)
        self.assertEqual(value, expected_value)
