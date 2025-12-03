#!/usr/bin/env python3
import sys

print("year,max_temp,max_temp_date")

current_year = None
max_temp = -9999
max_date = ""

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
        print(f"{current_year},{max_temp},{max_date}")
        current_year = year
        max_temp = temp
        max_date = date
    else:
        if temp > max_temp:
            max_temp = temp
            max_date = date

# flush last year
if current_year is not None:
    print(f"{current_year},{max_temp},{max_date}")
