import pandas as pd
import numpy as np

# Load Dataset

INPUT_PATH = "data/raw/train.csv"
OUTPUT_PATH = "data/processed/cleaned_delivery.csv"

df = pd.read_csv(INPUT_PATH)

print("=" * 60)
print("Original Shape:", df.shape)
print("=" * 60)

# Remove duplicate rows

df.drop_duplicates(inplace=True)

# Remove leading/trailing spaces
object_cols = df.select_dtypes(include="object").columns

for col in object_cols:
    df[col] = df[col].astype(str).str.strip()

# Replace missing representations
df.replace(["NaN", "nan", "", "NULL", "null"], np.nan, inplace=True)

# Numeric conversion
numeric_columns = [
    "Delivery_person_Age",
    "Delivery_person_Ratings",
    "Vehicle_condition",
    "multiple_deliveries"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Clean Time Taken column
# Example:
# "30 (min)" -> 30

df["Time_taken(min)"] = (
    df["Time_taken(min)"]
      .astype(str)
      .str.extract(r"(\d+)")
      .astype(float)
)

# Convert Date

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    dayfirst=True,
    errors="coerce"
)

# Convert Time Columns
for col in ["Time_Orderd", "Time_Order_picked"]:
    df[col] = pd.to_datetime(
        df[col],
        format="%H:%M:%S",
        errors="coerce"
    )

# Fill Missing Value
df["Delivery_person_Age"].fillna(
    df["Delivery_person_Age"].median(),
    inplace=True
)

df["Delivery_person_Ratings"].fillna(
    df["Delivery_person_Ratings"].median(),
    inplace=True
)

df["Road_traffic_density"].fillna(
    df["Road_traffic_density"].mode()[0],
    inplace=True
)

df["Weatherconditions"].fillna(
    df["Weatherconditions"].mode()[0],
    inplace=True
)

df["Festival"].fillna(
    "No",
    inplace=True
)

df["City"].fillna(
    df["City"].mode()[0],
    inplace=True
)

df["multiple_deliveries"].fillna(
    0,
    inplace=True
)

# Remove Invalid Ratings
df = df[
    (df["Delivery_person_Ratings"] >= 1)
    &
    (df["Delivery_person_Ratings"] <= 5)
]

# Remove Invalid Ages
df = df[
    (df["Delivery_person_Age"] >= 18)
    &
    (df["Delivery_person_Age"] <= 70)
]

# Remove Invalid Coordinates
df = df[
    (df["Restaurant_latitude"] != 0)
    &
    (df["Restaurant_longitude"] != 0)
]

# ==========================================
# Reset Index
# ==========================================

df.reset_index(drop=True, inplace=True)

# Save Cleaned Dataset
df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("=" * 60)
print("Cleaned Shape:", df.shape)
print("Saved to:", OUTPUT_PATH)
print("=" * 60)

print(df.head())