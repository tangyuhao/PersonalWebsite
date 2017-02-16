mysql -u root -p -e "DROP DATABASE IF EXISTS test_db;"
mysql -u root -p -e "CREATE DATABASE test_db;"
mysql -u root -p test_db < tbl_create.sql
mysql -u root -p test_db < load_data.sql

