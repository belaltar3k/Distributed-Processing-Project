import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# 1) Read raw CSV
df = pd.read_csv("toronto_climate1963_2013.csv")

# 2) Drop columns we don't need (flags + gusts + some metadata)
columns_to_drop = [
    "Data Quality",
    "Max Temp Flag", "Min Temp Flag", "Mean Temp Flag",
    "Heat Deg Days Flag", "Cool Deg Days Flag",
    "Total Rain Flag", "Total Snow Flag", "Total Precip Flag",
    "Snow on Grnd Flag",
    "Dir of Max Gust Flag", "Spd of Max Gust Flag",
    "Dir of Max Gust (10s deg)", "Spd of Max Gust (km/h)",
    "Heat Deg Days (°C)", "Cool Deg Days (°C)",
    # metadata columns we don't really need for analysis/MapReduce
    "Longitude (x)", "Latitude (y)",
    "Station Name", "Climate ID",
]

df = df.drop(columns=[c for c in columns_to_drop if c in df.columns])

# 3) Make sure Date/Time is proper datetime
df["Date/Time"] = pd.to_datetime(df["Date/Time"], errors="coerce")

# Rebuild Year / Month / Day from Date/Time (to be sure they are consistent)
df["Year"] = df["Date/Time"].dt.year
df["Month"] = df["Date/Time"].dt.month
df["Day"] = df["Date/Time"].dt.day

# 4) Impute missing numeric values with mean
num_cols = df.select_dtypes(include=["float64", "int64"]).columns
imputer_num = SimpleImputer(strategy="mean")
df[num_cols] = imputer_num.fit_transform(df[num_cols])

# 5) Impute missing categorical values (object) with most frequent
cat_cols = df.select_dtypes(include="object").columns
if len(cat_cols) > 0:
    imputer_cat = SimpleImputer(strategy="most_frequent")
    df[cat_cols] = imputer_cat.fit_transform(df[cat_cols])

# 6) Keep only the columns we actually care about
#    (you can add/remove here depending on what you want later)
cols_to_keep = [
    "Year", "Month", "Day",
    "Max Temp (°C)", "Min Temp (°C)", "Mean Temp (°C)",
    "Total Rain (mm)", "Total Snow (cm)", "Total Precip (mm)",
    "Snow on Grnd (cm)",
]

df = df[cols_to_keep]

# 7) Rename columns to simpler, Hadoop-friendly names
df = df.rename(columns={
    "Max Temp (°C)": "max_temp",
    "Min Temp (°C)": "min_temp",
    "Mean Temp (°C)": "mean_temp",
    "Total Rain (mm)": "total_rain_mm",
    "Total Snow (cm)": "total_snow_cm",
    "Total Precip (mm)": "total_precip_mm",
    "Snow on Grnd (cm)": "snow_on_ground_cm",
})

# 8) Just in case: drop any row where year or max_temp is still missing
df = df.dropna(subset=["Year", "max_temp"])

# 9) Sort by date
df = df.sort_values(["Year", "Month", "Day"])

# 10) Save cleaned data
df.to_csv("toronto_climate.csv", index=False)

print("Saved cleaned file as toronto_climate.csv")
