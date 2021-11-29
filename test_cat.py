import pandas as pd
import unittest
import numpy as np
import csv

# Creating the dataframe
df = pd.read_csv('C:\\Users\\mishr\\PycharmProjects\\pytest\\demo_data_churn.csv', engine='python')
gkk = df.groupby(['region', 'volume_in_kg']).first()

sum_val = df.groupby('region')['volume_in_kg'].sum()
mean_val = df.groupby('region')['volume_in_kg'].mean()
med_val = df.groupby('region')['volume_in_kg'].median()
min_val = df.groupby('region')['volume_in_kg'].min()
max_val = df.groupby('region')['volume_in_kg'].max()
std_val = df.groupby('region')['volume_in_kg'].std()
var_val = df.groupby('region')['volume_in_kg'].var()


class TestingSum(unittest.TestCase):

    def test_negativeForLess(self):
        x = min_val
        y = 0

        if (x < y).any():
            raise Exception("error: Min value cannot be in minus", + min_val)
        else:
            return "correct: Min value is positive "

    def test_negativeFor(self):
        x = min_val
        y = 0

        if (x < y).all():
            raise Exception("error: Min value cannot be in minus", + min_val)
        else:
            return "correct: Min value is positive "


if __name__ == '__main__':
    unittest.main()

