import unittest
from statistics import mean
import numpy
import pandas as pd
csv = 'demo_data_churn.csv'

df2 = pd.read_csv(csv)
su = df2['gross_sales'].sum()
print("Total Sales:", round(su))
