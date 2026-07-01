-- Revenue by City

SELECT
City,
SUM(Revenue)
FROM delivery_data
GROUP BY City
ORDER BY SUM(Revenue) DESC;

-- Revenue by Payment

SELECT
Payment_Method,
SUM(Revenue)
FROM delivery_data
GROUP BY Payment_Method;

-- Driver Performance

SELECT
Delivery_person_ID,
COUNT(*) Orders,
AVG(Driver_Efficiency) Efficiency
FROM delivery_data
GROUP BY Delivery_person_ID;

-- Vehicle Performance

SELECT
Type_of_vehicle,
AVG(Time_taken_min)
FROM delivery_data
GROUP BY Type_of_vehicle;

-- Festival Impact

SELECT
Festival,
AVG(Time_taken_min),
SUM(Revenue)
FROM delivery_data
GROUP BY Festival;

-- Weather Impact

SELECT
Weatherconditions,
AVG(Time_taken_min)
FROM delivery_data
GROUP BY Weatherconditions;

-- Traffic Impact

SELECT
Road_traffic_density,
AVG(Time_taken_min)
FROM delivery_data
GROUP BY Road_traffic_density;

-- Peak Hour

SELECT
Peak_Hour,
COUNT(*)
FROM delivery_data
GROUP BY Peak_Hour;

-- Weekend Revenue

SELECT
Weekend,
SUM(Revenue)
FROM delivery_data
GROUP BY Weekend;

-- Top Cities

SELECT
City,
AVG(Driver_Score)
FROM delivery_data
GROUP BY City;