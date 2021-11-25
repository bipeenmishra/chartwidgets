import unittest
from statistics import mean
import numpy
import pandas as pd

df2 = pd.read_csv('C:\\Users\\mishr\\Downloads\\demo_data_churn.csv', engine='python')
su = df2['gross_sales'].sum()
me = df2['gross_sales'].mean()
mi = df2['gross_sales'].min()
mx = df2['gross_sales'].max()
med = df2['gross_sales'].median()
st = df2['gross_sales'].std()
va = df2['gross_sales'].var()
sum_val = 2719153786.144917
mean_val = 8350.209238282016
max_val = 3077822.953
min_val = -3221995.235
median_val = 1810.978448
std_val = 29363.13365365425
var_val = 862193617.9623628


# Testing for sales data


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
