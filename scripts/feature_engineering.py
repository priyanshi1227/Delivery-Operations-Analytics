import pandas as pd
import numpy as np

INPUT_PATH = "data/processed/cleaned_delivery.csv"
OUTPUT_PATH = "data/processed/delivery_features.csv"

df = pd.read_csv(INPUT_PATH)

# Date Columns

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Time_Orderd"] = pd.to_datetime(
    df["Time_Orderd"],
    errors="coerce"
)

# Calendar Features
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.month_name()

df["Day"] = df["Order_Date"].dt.day

df["Weekday"] = df["Order_Date"].dt.day_name()

df["Quarter"] = df["Order_Date"].dt.quarter

# Order Hour

df["Order_Hour"] = df["Time_Orderd"].dt.hour

# Weekend
df["Weekend"] = np.where(
    df["Weekday"].isin(["Saturday", "Sunday"]),
    1,
    0
)

# Peak Hour

df["Peak_Hour"] = np.where(
    (
        (df["Order_Hour"] >= 11)
        &
        (df["Order_Hour"] <= 14)
    )
    |
    (
        (df["Order_Hour"] >= 18)
        &
        (df["Order_Hour"] <= 22)
    ),
    "Peak",
    "Non Peak"
)

# Driver Rating Category
df["Rating_Category"] = pd.cut(
    df["Delivery_person_Ratings"],
    bins=[0,3.5,4.2,5],
    labels=[
        "Low",
        "Average",
        "Excellent"
    ]
)

# Driver Age Group
df["Age_Group"] = pd.cut(
    df["Delivery_person_Age"],
    bins=[18,25,35,45,60,70],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-60",
        "60+"
    ]
)

# Distance (Approximation)
df["Distance"] = np.sqrt(
    (
        df["Restaurant_latitude"]
        -
        df["Delivery_location_latitude"]
    )**2
    +
    (
        df["Restaurant_longitude"]
        -
        df["Delivery_location_longitude"]
    )**2
)

# Distance Category
df["Distance_Category"] = pd.cut(
    df["Distance"],
    bins=[0,0.05,0.10,0.20,10],
    labels=[
        "Short",
        "Medium",
        "Long",
        "Very Long"
    ]
)

# Delivery Speed

df["Delivery_Speed"] = (
    df["Distance"] /
    df["Time_taken(min)"]
)

# Late Delivery
df["Late_Delivery"] = np.where(
    df["Time_taken(min)"] > 40,
    1,
    0
)

# High Traffic

df["High_Traffic"] = np.where(
    df["Road_traffic_density"].isin(
        ["Jam","High"]
    ),
    1,
    0
)

# Multiple Orders
df["Multiple_Order"] = np.where(
    df["multiple_deliveries"] > 1,
    1,
    0
)

# Festival Order
df["Festival_Order"] = np.where(
    df["Festival"] == "Yes",
    1,
    0
)

# Vehicle Score
vehicle_score = {
    "motorcycle":4,
    "scooter":3,
    "electric_scooter":5,
    "bicycle":2
}

df["Vehicle_Score"] = (
    df["Type_of_vehicle"]
      .astype(str)
      .str.lower()
      .map(vehicle_score)
)

# Driver Efficiency
df["Driver_Efficiency"] = (
    df["Delivery_person_Ratings"] * 10
) / df["Time_taken(min)"]

# Save Dataset

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("=" * 60)
print("Feature Engineered Dataset Saved")
print(df.shape)
print("=" * 60)

print(df.head())