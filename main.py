'''
4276814.csv is average NJ temperature data from 2023-06-01 to 2025-12-31
4283629.csv is from 2021-01-01 to 2023-05-31
See temperature trends
    - Calculate average temperatures for each year
    - Maybe take data from the end of 2025 and compare it with temp. data from the middle of 2023
Try to predict future NJ temperature trends
    - Maybe try to predict temperatures for 2030
'''
from pprint import pprint
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

def calc_avg(ls: list[int, int]) -> int:
    return ls[0]/ls[1]

df = pd.concat([pd.read_csv("4276814.csv"), pd.read_csv("4283629.csv")], ignore_index = True, sort = False) # takes both csv files, combines them into one dataframe

data = df.to_dict(orient="records") # turns df into list of dicts

year_total_count = {str(i): [0, 0] for i in range(2021, 2026)} # first is total, second is count, used for tracking the average for each year; data from 2021 to 2025

# Using DATE, TAVG
# Finds average for each year
for dat in data:
    if pd.isna(dat['TAVG']):
        continue
    
    date = str(dat['DATE'])
    tavg = dat['TAVG']

    year_total_count[date][1] += 1
    year_total_count[date][0] += tavg


tmps = [] # temperature list
yrs = [int(i) for i in year_total_count]

for yr in yrs:
    tmps.append(calc_avg(year_total_count[str(yr)]))

slope, intercept, r, p, std_err = stats.linregress(yrs, tmps)

print(f"\n2030 avg. temperature: {slope * 2030 + intercept}")

# tmpmodel = list(map(lambda x: slope * x + intercept, yrs))