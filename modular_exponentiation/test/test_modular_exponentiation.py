import unittest
from nose_parameterized import parameterized
from app.modular_exponentiation import exponentiate

class TestModularExponentiation(unittest.TestCase):
    @parameterized.expand([
        [3, 3, 2, 1],
        [3, 5, 7, 5],
        [1, 1, 1, 1],
        [2, 2, -3, -1],
        [-2, 3, 5, -4],
        [-2, 3, -5, 4],
        [0, 2, 3, 0],
        [3, 0, 3, 1],
    ])
    def test_exponentiate(self, base, exponent, modulus, expected_result):
        self.assertEqual(exponentiate(base, exponent, modulus), base ** exponent % modulus)

    def test_root_is_rejected(self):
        with self.assertRaisesRegexp(ValueError, 'Calculating roots is not supported, the exponent must not be negative.'):
            exponentiate(49, -2, 5)
