#!/usr/bin/env python3
import sys

print("year,avg_mean_temp,total_precip")  # CSV header

current_year = None
temp_sum = 0.0
temp_count = 0
precip_total = 0.0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    year, values = line.split("\t")
    mean_str, precip_str = values.split(",")

    try:
        mean_temp = float(mean_str)
    except:
        continue  # skip invalid values

    try:
        precip = float(precip_str)
    except:
        precip = 0.0

    if current_year is None:
        current_year = year

    # When year changes → output previous year
    if year != current_year:
        avg = temp_sum / temp_count if temp_count > 0 else ""
        print(f"{current_year},{avg},{precip_total}")

        # reset
        current_year = year
        temp_sum = 0.0
        temp_count = 0
        precip_total = 0.0

    # accumulate
    temp_sum += mean_temp
    temp_count += 1
    precip_total += precip

# flush last year
if current_year is not None:
    avg = temp_sum / temp_count if temp_count > 0 else ""
    print(f"{current_year},{avg},{precip_total}")
