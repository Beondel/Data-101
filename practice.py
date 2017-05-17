import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('./single_family_residences_07076.csv')
print(df)
houseValues = [x for x in df['Value']]
yearMonthDays = []
for i in df['Date']:
    stringDate = str(i)
    yearMonthDays.append(stringDate.split("-"))

houseValues = list(reversed(houseValues))
yearMonthDays = list(reversed(yearMonthDays))
print(houseValues)
print(yearMonthDays)

intDateList = [int(''.join(x)) for x in yearMonthDays]
print(intDateList)
plt.plot(intDateList, houseValues)
plt.show()
