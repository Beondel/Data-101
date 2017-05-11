import pandas as pn
import numpy as np

numbers = [1, 2, 3, 4, 5]
print(np.mean(numbers))
print(np.median(numbers))
print(np.std(numbers))

import pandas as pd


series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
print(series)


series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                   index=['Instructor', 'Curriculum Manager',
                          'Course Number', 'Power Level'])
print(series)


series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                   index=['Instructor', 'Curriculum Manager',
                          'Course Number', 'Power Level'])
print(series['Instructor'])
print("")
print(series[['Instructor', 'Curriculum Manager', 'Course Number']])


cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig',
                                             'Puppy', 'Kitten'])
print(cuteness > 3)
print("")
print(cuteness[cuteness > 3])
