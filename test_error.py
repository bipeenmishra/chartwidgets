import unittest
from statistics import mean
import numpy
import pandas as pd
csv = 'demo_data_churn.csv'
df2 = pd.read_csv(csv)
sum_val = df2['volume_in_kg'].sum()
min_val = df2['volume_in_kg'].min()
var_val = df2['volume_in_kg'].var()

# Testing for margin data


class TestingSum(unittest.TestCase):
    def test_negativeForLess(self):
        x = min_val
        y = 0

        if x < y:
            raise Exception("Error: Min value is less than zero ", min_val)
        else:
            return "correct: Min value is positive "

    def test_positiveForGreater(self):
        x = sum_val
        y = 10000000

        if x > y:
            raise Exception("error: Sum of volume cannot be too high ", sum_val)
        else:
            return "correct: Sum of volume in range"

    def test_positiveForGre(self):
        x = var_val
        y = 10000000

        if x > y:
            raise Exception("error: Var of volume cannot be too high ", var_val)
        else:
            return "correct: Var of volume in range"


if __name__ == '__main__':
    unittest.main()
