import unittest
from calculate_volts import calculate_volts


class TestCalculateVolts(unittest.TestCase):
    def test_valid_input(self):
        # Test valid input combinations
        self.assertEqual(calculate_volts(amps=2, ohms=3), 6)
        self.assertEqual(calculate_volts(amps=2, watts=12, ohms=3), 6)
        self.assertAlmostEqual(calculate_volts(watts=36, ohms=9), 18, places=5)

    def test_invalid_input(self):
        # Test invalid input types
        with self.assertRaises(TypeError):
            calculate_volts(amps="2", ohms=3)

        with self.assertRaises(TypeError):
            calculate_volts(amps=2, ohms="3")

        with self.assertRaises(TypeError):
            calculate_volts(watts="12", ohms=3)


if __name__ == "__main__":
    unittest.main()
