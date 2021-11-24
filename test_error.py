import unittest
from statistics import mean
import numpy
import pandas as pd
df2 = pd.read_csv('C:\\Users\\mishr\\Downloads\\demo_data_churn.csv', engine='python')
sum_val = 1457317609.7210157
min_val = -4069043.765
var_val = 586680528.3043605

# Testing for margin data


class TestingSum(unittest.TestCase):
    def test_negativeForLess(self):
        first = min_val
        second = 0

        if first < second:
            return "error: value is less than second value"
        else:
            return "correct: value is greater than second value"

    def test_positiveForGreater(self):
        first = sum_val
        second = 10000000

        if first > second:
            return "error: value is Greater than second value "
        else:
            return "correct: value is less than second value"

    def test_positiveForGre(self):
        first = var_val
        second = 10000000

        if first > second:
            return "error: value is Greater than second value "
        else:
            return "correct: value is less than second value"


if __name__ == '__main__':
    unittest.main()
