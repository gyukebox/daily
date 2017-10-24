from pandas import Series, DataFrame
import numpy as np
import pandas as pd

# basic Series example
france = Series([10, 12, 3, 15], index=['Zidane', 'Henry', 'Lizarazu', 'Thuram'])
print(france)
print(france.values)
print(france.index)
# value by index
print(france['Lizarazu'])
