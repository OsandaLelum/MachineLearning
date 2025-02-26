# -*- coding: utf-8 -*-
"""PandasDF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aZOnH78UlX9KUdvKGBLrpQ_8bwpHdWCL
"""

import pandas as pd

data = {
    'Region': ['North', 'South', 'West', 'North', 'South', 'West', 'North'],
    'Product': ['A', 'B', 'C', 'B', 'C', 'A', 'C'],
    'Sales': [80, 150, 130, 90, 110, 120, 130]
}

df = pd.DataFrame(data)

print(df)


for region, group in df.groupby( 'Region'):
 with pd.ExcelWriter(f"sales_{region}.xlsx") as writer:
  group.to_excel (writer, index=False)