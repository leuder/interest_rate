import unittest

from pynterest_rate import Compound

class TestCompoundClass(unittest.TestCase):
    def setUp(self):
        self.compound = Compound(0.05, 1, 22.517)

    def test_futurevaluecalculation(self):
        self.assertEqual(
            round(self.compound.calulate_future_value()), 3, 'calculated future value not as expected'
        )

if __name__ == '__main__':
    unittest.main()