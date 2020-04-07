#!/bin/sh
mysql -h78.46.250.83 -ugroupproject -pBierkeet42069! --local_infile=1 hu_recommendations -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE './csv/products.csv' INTO TABLE products FIELDS TERMINATED BY '#' (product_id)"
