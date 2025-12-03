#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    if line.startswith("Year,Month,Day"):
        continue

    parts = line.split(",")
    if len(parts) < 6:
        continue

    year_str = parts[0]
    month_str = parts[1]
    day_str = parts[2]
    min_temp_str = parts[4]

    try:
        min_temp = float(min_temp_str)
    except:
        continue

    try:
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
        date = f"{year:04d}-{month:02d}-{day:02d}"
    except:
        date = f"{year_str}-{month_str}-{day_str}"

    print(f"{year_str}\t{min_temp},{date}")
