USE delivery_operations;

CREATE TABLE delivery_data (

ID VARCHAR(30),

Delivery_person_ID VARCHAR(30),

Delivery_person_Age INT,

Delivery_person_Ratings DECIMAL(3,2),

Restaurant_latitude DOUBLE,

Restaurant_longitude DOUBLE,

Delivery_location_latitude DOUBLE,

Delivery_location_longitude DOUBLE,

Order_Date DATE,

Time_Orderd TIME,

Time_Order_picked TIME,

Weatherconditions VARCHAR(50),

Road_traffic_density VARCHAR(30),

Vehicle_condition INT,

Type_of_order VARCHAR(30),

Type_of_vehicle VARCHAR(30),

multiple_deliveries INT,

Festival VARCHAR(10),

City VARCHAR(30),

Time_taken_min INT,

Year INT,

Month INT,

Month_Name VARCHAR(20),

Day INT,

Weekday VARCHAR(20),

Quarter INT,

Order_Hour INT,

Weekend INT,

Peak_Hour VARCHAR(20),

Rating_Category VARCHAR(20),

Age_Group VARCHAR(20),

Distance DOUBLE,

Distance_Category VARCHAR(20),

Delivery_Speed DOUBLE,

Late_Delivery INT,

High_Traffic INT,

Multiple_Order INT,

Festival_Order INT,

Vehicle_Score INT,

Driver_Efficiency DOUBLE,

Customer_ID VARCHAR(30),

Restaurant_ID VARCHAR(30),

Order_Value DOUBLE,

Delivery_Fee DOUBLE,

Tip DOUBLE,

Packaging_Fee DOUBLE,

Discount DOUBLE,

Payment_Method VARCHAR(30),

Order_Status VARCHAR(20),

Revenue DOUBLE,

On_Time VARCHAR(10),

Driver_Score DOUBLE,

Revenue_Per_Minute DOUBLE,

Revenue_Per_KM DOUBLE,

Order_Bucket VARCHAR(20)

);