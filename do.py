import pandas as pd
import os

filesdir = 'data/EPL/2018-19/E0.csv'

df = pd.read_csv(filesdir)

print(df.shape)
print(df.count())