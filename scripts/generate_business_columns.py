import pandas as pd
import numpy as np

np.random.seed(42)

INPUT_PATH = "data/processed/delivery_features.csv"
OUTPUT_PATH = "data/processed/final_delivery_dataset.csv"

df = pd.read_csv(INPUT_PATH)

print("="*60)
print("Generating Business Columns")
print("="*60)

# -------------------------------
# Customer ID
# -------------------------------

customers = [f"CUST{100000+i}" for i in range(3500)]

df["Customer_ID"] = np.random.choice(
    customers,
    len(df)
)

# -------------------------------
# Restaurant ID
# -------------------------------

restaurants = [f"REST{1000+i}" for i in range(700)]

df["Restaurant_ID"] = np.random.choice(
    restaurants,
    len(df)
)

# -------------------------------
# Order Value (₹)
# -------------------------------

df["Order_Value"] = np.random.randint(
    150,
    1800,
    len(df)
)

# -------------------------------
# Delivery Fee
# -------------------------------

conditions = [
    df["Distance"] <= 0.05,
    (df["Distance"] > 0.05) & (df["Distance"] <= 0.10),
    df["Distance"] > 0.10
]

fees = [25,45,70]

df["Delivery_Fee"] = np.select(
    conditions,
    fees,
    default=40
)

# -------------------------------
# Tip
# -------------------------------

df["Tip"] = (
    df["Order_Value"]
    *
    np.random.uniform(
        0.02,
        0.15,
        len(df)
    )
).round(2)

# -------------------------------
# Packaging Fee
# -------------------------------

df["Packaging_Fee"] = np.random.randint(
    10,
    40,
    len(df)
)

# -------------------------------
# Discount
# -------------------------------

discount = np.random.choice(
    [0,20,50,75,100],
    len(df),
    p=[0.35,0.25,0.20,0.10,0.10]
)

df["Discount"] = discount

# -------------------------------
# Payment Method
# -------------------------------

payment = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Wallet"
]

df["Payment_Method"] = np.random.choice(
    payment,
    len(df),
    p=[0.50,0.15,0.10,0.15,0.10]
)

# -------------------------------
# Order Status
# -------------------------------

status = [
    "Delivered",
    "Cancelled"
]

df["Order_Status"] = np.random.choice(
    status,
    len(df),
    p=[0.97,0.03]
)

# -------------------------------
# Revenue
# -------------------------------

df["Revenue"] = (

    df["Order_Value"]

    +

    df["Delivery_Fee"]

    +

    df["Packaging_Fee"]

    +

    df["Tip"]

    -

    df["Discount"]

)

# -------------------------------
# On-Time Delivery
# -------------------------------

df["On_Time"] = np.where(
    df["Time_taken(min)"] <= 40,
    "Yes",
    "No"
)

# -------------------------------
# Driver Score
# -------------------------------

df["Driver_Score"] = (
    (
        df["Delivery_person_Ratings"]*20
    )
    +
    (
        100-df["Time_taken(min)"]
    )
).round(2)

# -------------------------------
# Revenue Per Minute
# -------------------------------

df["Revenue_Per_Minute"] = (
    df["Revenue"] /
    df["Time_taken(min)"]
).round(2)

# -------------------------------
# Revenue Per KM
# -------------------------------

df["Revenue_Per_KM"] = (
    df["Revenue"] /
    (df["Distance"]+0.001)
).round(2)

# -------------------------------
# Order Bucket
# -------------------------------

df["Order_Bucket"] = pd.cut(

    df["Order_Value"],

    bins=[0,300,600,1000,5000],

    labels=[
        "Budget",
        "Standard",
        "Premium",
        "Luxury"
    ]

)

# -------------------------------
# Save
# -------------------------------

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print(df.head())

print("="*60)
print("Final Shape:",df.shape)
print("="*60)