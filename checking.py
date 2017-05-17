import pandas as pd
import numpy as np

titanic = pd.read_csv('./titanic_data.csv')
print(np.mean(titanic['Age']))
titanic['Age'] = titanic['Age'].fillna(np.mean(titanic['Age']))

print(titanic)
