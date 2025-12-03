#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # skip header
    if line.startswith("Year,Month,Day"):
        continue

    parts = line.split(",")
    if len(parts) < 9:
        continue

    year = parts[0]
    # month = parts[1]  # not needed here
    # day = parts[2]
    # max_temp = parts[3]
    # min_temp = parts[4]
    mean_temp_str = parts[5]
    total_precip_str = parts[8]  # total_precip_mm

    try:
        mean_temp = float(mean_temp_str)
    except:
        # if mean is missing, skip this day for avg
        continue

    try:
        total_precip = float(total_precip_str)
    except:
        total_precip = 0.0

    # key = year, value = "mean_temp,total_precip"
    print(f"{year}\t{mean_temp},{total_precip}")
