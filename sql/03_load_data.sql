USE delivery_operations;

LOAD DATA LOCAL INFILE
'C:/Users/YourName/Delivery-Operations-Analytics/data/processed/final_delivery_dataset.csv'

INTO TABLE delivery_data

FIELDS TERMINATED BY ','

ENCLOSED BY '"'

LINES TERMINATED BY '\n'

IGNORE 1 ROWS;