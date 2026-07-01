CREATE INDEX idx_driver
ON delivery_data(Delivery_person_ID);

CREATE INDEX idx_customer
ON delivery_data(Customer_ID);

CREATE INDEX idx_restaurant
ON delivery_data(Restaurant_ID);

CREATE INDEX idx_city
ON delivery_data(City);

CREATE INDEX idx_date
ON delivery_data(Order_Date);

CREATE INDEX idx_payment
ON delivery_data(Payment_Method);