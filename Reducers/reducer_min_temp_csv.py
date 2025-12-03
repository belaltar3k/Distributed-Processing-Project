#!/usr/bin/env python3
import sys

print("year,min_temp,min_temp_date")

current_year = None
min_temp = 9999
min_date = ""

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    year, value = line.split("\t")
    temp_str, date = value.split(",")

    try:
        temp = float(temp_str)
    except:
        continue

    if current_year is None:
        current_year = year

    if year != current_year:
        print(f"{current_year},{min_temp},{min_date}")
        current_year = year
        min_temp = temp
        min_date = date
    else:
        if temp < min_temp:
            min_temp = temp
            min_date = date

# flush last
if current_year is not None:
    print(f"{current_year},{min_temp},{min_date}")
