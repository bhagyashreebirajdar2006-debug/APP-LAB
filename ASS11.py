
import pandas as pd
import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))

series = pd.Series(numbers)

print("Pandas Series with ten random numbers:")
print(series)
