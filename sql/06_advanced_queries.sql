-- Top Drivers

SELECT

Delivery_person_ID,

AVG(Driver_Score) Score,

RANK() OVER(
ORDER BY AVG(Driver_Score) DESC
) Ranking

FROM delivery_data

GROUP BY Delivery_person_ID;

-- Top Customers

SELECT

Customer_ID,

SUM(Revenue)

FROM delivery_data

GROUP BY Customer_ID

ORDER BY SUM(Revenue) DESC

LIMIT 10;

-- Top Restaurants

SELECT

Restaurant_ID,

SUM(Order_Value)

FROM delivery_data

GROUP BY Restaurant_ID

ORDER BY SUM(Order_Value) DESC

LIMIT 10;

-- Monthly Revenue

SELECT

Month_Name,

SUM(Revenue)

FROM delivery_data

GROUP BY Month_Name

ORDER BY Month;

-- Revenue by Order Bucket

SELECT

Order_Bucket,

SUM(Revenue)

FROM delivery_data

GROUP BY Order_Bucket;

-- Highest Rated Drivers

SELECT

Delivery_person_ID,

AVG(Delivery_person_Ratings)

FROM delivery_data

GROUP BY Delivery_person_ID

ORDER BY AVG(Delivery_person_Ratings) DESC;

-- On-Time %

SELECT

ROUND(

SUM(
CASE
WHEN On_Time='Yes'
THEN 1
ELSE 0
END
)*100/COUNT(*)

,2)

AS SLA;

-- Late Deliveries

SELECT

City,

COUNT(*)

FROM delivery_data

WHERE Late_Delivery=1

GROUP BY City;

-- Revenue per KM

SELECT

City,

AVG(Revenue_Per_KM)

FROM delivery_data

GROUP BY City;

-- Driver Leaderboard

SELECT

Delivery_person_ID,

COUNT(*) Orders,

SUM(Revenue) Revenue,

AVG(Driver_Score) Score

FROM delivery_data

GROUP BY Delivery_person_ID

ORDER BY Revenue DESC;