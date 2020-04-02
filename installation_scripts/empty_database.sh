mysql -ugroupproject -pBierkeet42069! --local_infile=1 huwebshop -e "DELETE FROM profiles; DELETE FROM previously_recommended; DELETE FROM viewed_before; DELETE FROM order;
DELETE FROM viewed_brand; DELETE FROM viewed_category; DELETE FROM viewed_gender; DELETE FROM viewed_product_size; DELETE FROM viewed_product_type;
DELETE FROM viewed_promos; viewed_sub_category; DELETE FROM viewed_sub_sub_category; DELETE FROM viewed_type; DELETE FROM sessions; DELETE FROM products;
"
