# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:10:14 2021

@author: 翟君伟
"""


import pandas as pd
filepath = "earthquakes-2021-10-17_10-20-59_+0800.tsv"
data = pd.read_csv(filepath, sep='\t')
data = data.iloc[1:]

#q1
death_data = data[["Country","Deaths"]]
death_sum_by_country= death_data.groupby("Country").sum()
death_sum_by_country.sort_values(by=["Deaths"],ascending=False,inplace=True)
print(death_sum_by_country.head(10))

#q2
mag_of_year = data[["Year","Mag"]]
mag_of_year_count = mag_of_year[mag_of_year["Mag"] > 6 ].groupby(by = ['Year']).count()
print(mag_of_year_count)

#q3
def CountEq_LargestEq(Country):
    data = pd.read_csv(filepath, sep='\t')
    data = data.iloc[1:]
    mag_of_country =data[data["Country"] == Country]
    count = mag_of_country["Mag"].count()

    max_data = mag_of_country[mag_of_country["Mag"] == mag_of_country["Mag"].max()]
    date = max_data[["Year","Mo","Dy"]]
    return count,date
count,date =CountEq_LargestEq("CHINA")
print(count)

print(date)