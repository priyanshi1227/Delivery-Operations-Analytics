-- Total Orders
SELECT COUNT(*) FROM delivery_data;

-- Total Drivers
SELECT COUNT(DISTINCT Delivery_person_ID)
FROM delivery_data;

-- Total Customers
SELECT COUNT(DISTINCT Customer_ID)
FROM delivery_data;

-- Total Restaurants
SELECT COUNT(DISTINCT Restaurant_ID)
FROM delivery_data;

-- Average Delivery Time
SELECT AVG(Time_taken_min)
FROM delivery_data;

-- Average Rating
SELECT AVG(Delivery_person_Ratings)
FROM delivery_data;

-- Revenue
SELECT SUM(Revenue)
FROM delivery_data;

-- Average Order Value
SELECT AVG(Order_Value)
FROM delivery_data;

-- Orders by City
SELECT City,COUNT(*)
FROM delivery_data
GROUP BY City;

-- Orders by Vehicle
SELECT Type_of_vehicle,
COUNT(*)
FROM delivery_data
GROUP BY Type_of_vehicle;