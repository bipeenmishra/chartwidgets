import unittest
from statistics import mean
import numpy
import pandas as pd
csv = 'demo_data_churn.csv'

df2 = pd.read_csv(csv)
su = df2['gm'].sum()
me = df2['gm'].mean()
mi = df2['gm'].min()
mx = df2['gm'].max()
med = df2['gm'].median()
st = df2['gm'].std()
va = df2['gm'].var()
sum_val = 1457317609.7210157
mean_val = 4475.255143643776
max_val = 3073251.674
min_val = -4069043.765
median_val = 760.69374
std_val = 24221.48897785519
var_val = 586680528.3043605

# Testing for margin data


class TestingSum(unittest.TestCase):

    def test_sum(self):
        if su == sum_val:
            return "Value is match"
        else:
            return "Error: Value is not match"

    def test_mean(self):
        if me == min_val:
            return "Value is match"
        else:
            return "Error: Value is not match"

    def test_min(self):
        if mi == min_val:
            return "Value is match"
        else:
            return "Error: Value is not match"

    def test_max(self):
        if mx == max_val:
            return "Value is match"
        else:
            return "Error: Value is not match"

    def test_median(self):
        if med == median_val:
            return "Value is match"
        else:
            return "Error: Value is not match"

    def test_std(self):
        if st == std_val:
            return "Value is match"
        else:
            return "Error: Value is not match"

    def test_var(self):
        if va == var_val:
            return "Value is match"
        else:
            return "Error: Value is not match"


if __name__ == '__main__':
    unittest.main()
