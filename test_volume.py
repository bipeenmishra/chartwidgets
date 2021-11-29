import unittest
from statistics import mean
import numpy
import pandas as pd
csv = 'demo_data_churn.csv'

df2 = pd.read_csv(csv)
su = df2['volume_in_kg'].sum()
me = df2['volume_in_kg'].mean()
mi = df2['volume_in_kg'].min()
mx = df2['volume_in_kg'].max()
med = df2['volume_in_kg'].median()
st = df2['volume_in_kg'].std()
va = df2['volume_in_kg'].var()
sum_val = 256677722.91003045
mean_val = 788.2278317708805
max_val = 439245.0136
min_val = -1220509.226
median_val = 40.35166904
std_val = 6755.173313682895
var_val = 45632366.49789355

# Testing for volume data


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


