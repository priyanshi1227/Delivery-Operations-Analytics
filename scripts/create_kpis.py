import pandas as pd

INPUT_PATH = "data/processed/final_delivery_dataset.csv"
OUTPUT_PATH = "data/processed/dashboard_kpis.csv"

df = pd.read_csv(INPUT_PATH)

kpis = {

"Total Orders":[len(df)],

"Delivered Orders":[
len(
df[df["Order_Status"]=="Delivered"]
)
],

"Cancelled Orders":[
len(
df[df["Order_Status"]=="Cancelled"]
)
],

"Revenue":[
round(df["Revenue"].sum(),2)
],

"Average Order Value":[
round(df["Order_Value"].mean(),2)
],

"Average Delivery Time":[
round(df["Time_taken(min)"].mean(),2)
],

"Average Driver Rating":[
round(df["Delivery_person_Ratings"].mean(),2)
],

"Average Tip":[
round(df["Tip"].mean(),2)
],

"Average Delivery Fee":[
round(df["Delivery_Fee"].mean(),2)
],

"On Time %":[

round(

(
len(
df[df["On_Time"]=="Yes"]
)
/
len(df)
)
*100

,2)

],

"Average Driver Score":[
round(df["Driver_Score"].mean(),2)
]

}

kpi_df = pd.DataFrame(kpis)

kpi_df.to_csv(
OUTPUT_PATH,
index=False
)

print(kpi_df)