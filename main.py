'''
Data is average NJ temperature data from 2023-06-01 to 2025-12-31
See temperature trends
    - Calculate average temperatures for each year
    - Maybe take data from the end of 2025 and compare it with temp. data from the middle of 2023
Try to predict future NJ temperature trends
    - Maybe try to predict temperatures for 2030
'''

import matplotlib.pyplot as plt
from pprint import pprint
import pandas as pd

def calc_avg(ls: list[int, int]) -> int:
    return ls[0]/ls[1]

df = pd.read_csv("4276814.csv")

data = df.to_dict(orient="records") # turns df into list of dicts

year_total_count = {'2023': [0, 0], '2024': [0, 0], '2025':[0, 0]} # first is total, second is count, used for tracking the average for each year

# Using DATE, TAVG
# Finds average for each year
for dat in data:
    if pd.isna(dat['TAVG']):
        continue
    
    date = str(dat['DATE'])
    tavg = dat['TAVG']

    year_total_count[date][1] += 1
    year_total_count[date][0] += tavg


# Prints averages
for yr in range(2023, 2026):
    print(f"{yr}: {calc_avg(year_total_count[str(yr)])}")



# pprint(data)





# plt.plot(df["DATE"], df["TAVG"])
# plt.xlabel("Year")
# plt.ylabel("Average Temp.")

# plt.show()