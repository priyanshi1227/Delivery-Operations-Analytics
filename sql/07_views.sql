USE delivery_operations;

CREATE VIEW city_summary AS

SELECT

City,

COUNT(*) Total_Orders,

SUM(Revenue) Revenue,

AVG(Time_taken_min) Avg_Time,

AVG(Driver_Score) Avg_Driver_Score

FROM delivery_data

GROUP BY City;

--------------------------------------------------

CREATE VIEW driver_summary AS

SELECT

Delivery_person_ID,

COUNT(*) Orders,

AVG(Driver_Score) Driver_Score,

AVG(Delivery_person_Ratings) Rating,

SUM(Revenue) Revenue

FROM delivery_data

GROUP BY Delivery_person_ID;

--------------------------------------------------

CREATE VIEW restaurant_summary AS

SELECT

Restaurant_ID,

COUNT(*) Orders,

SUM(Order_Value) Sales,

AVG(Revenue) Revenue

FROM delivery_data

GROUP BY Restaurant_ID;