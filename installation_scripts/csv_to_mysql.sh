mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/profiles.csv' INTO TABLE profiles FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/products.csv' INTO TABLE products FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/sessions.csv' INTO TABLE sessions FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/order.csv' INTO TABLE order FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/viewed_brand.csv' INTO TABLE viewed_brand FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/viewed_category.csv' INTO TABLE viewed_category FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/viewed_gender.csv' INTO TABLE viewed_gender FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/sub_category.csv' INTO TABLE viewed_sub_category FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/viewed_sub_sub_category.csv' INTO TABLE viewed_sub_sub_category FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/viewed_promos.csv' INTO TABLE viewed_promos FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/viewed_type.csv' INTO TABLE viewed_type FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/viewed_product_type.csv' INTO TABLE viewed_product_type FIELDS TERMINATED BY ','"
mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "SET FOREIGN_KEY_CHECKS = 0; LOAD DATA LOCAL INFILE '../database/mongo_to_csv/csv/viewed_product_size.csv' INTO TABLE viewed_product_size FIELDS TERMINATED BY ','"
