-- Source_to_Bronze
INSERT INTO metadata.config_table(task_id, task_name, source_connection, 
				  source_database, source_schema, source_table, target_folder, load_type, enable, phase)
VALUES
(1, 'source_to_bronze', 'electronics_connection', 'Global_Electronics_Retailer', 'Customer', 'Customers', 'Customers', 'Full load', 1, 'CusDB -> Bronze'),
(2, 'source_to_bronze', 'electronics_connection', 'Global_Electronics_Retailer', 'Stores', 'Stores', 'Stores', 'Full load', 1, 'CusDB -> Bronze'),
(3, 'source_to_bronze', 'electronics_connection', 'Global_Electronics_Retailer', 'Stores', 'Products', 'Products', 'Full load', 1, 'CusDB -> Bronze'),
(4, 'source_to_bronze', 'electronics_connection', 'Global_Electronics_Retailer', 'Sales', 'Sales', 'Sales', 'Full load', 1, 'CusDB -> Bronze'),
(5, 'source_to_bronze', 'electronics_connection', 'Global_Electronics_Retailer', 'Sales', 'Exchange_Rates', 'Exchange_Rates', 'Full load', 1, 'CusDB -> Bronze')

-- Bronze_to_Silver
INSERT INTO metadata.config_table(task_id, task_name, source_connection, source_folder,target_database, target_schema, target_table, load_type, enable, phase)
VALUES
(6, 'bronze_to_silver', 'LH_Global_Electronics_Reatiler', 'Customers', 'LH_Global_Electronics_Reatiler', 'dbo', 'silver_customer', 'Full load', 1, 'Bronze -> Silver'),
(7, 'bronze_to_silver', 'LH_Global_Electronics_Reatiler', 'Stores', 'LH_Global_Electronics_Reatiler', 'dbo', 'silver_stores', 'Full load', 1, 'Bronze -> Silver'),
(8, 'bronze_to_silver', 'LH_Global_Electronics_Reatiler', 'Product', 'LH_Global_Electronics_Reatiler', 'dbo', 'silver_product', 'Full load', 1, 'Bronze -> Silver'),
(9, 'bronze_to_silver', 'LH_Global_Electronics_Reatiler', 'Sales', 'LH_Global_Electronics_Reatiler', 'dbo', 'silver_sales', 'Full load', 1, 'Bronze -> Silver'),
(10, 'bronze_to_silver', 'LH_Global_Electronics_Reatiler', 'Exchange_Rates', 'LH_Global_Electronics_Reatiler', 'dbo', 'silver_exchange_rates', 'Full load', 1, 'Bronze -> Silver')

-- Source database
UPDATE metadata.config_table
SET source_database = 'LH_Global_Electronics_Reatiler'
WHERE task_name = 'bronze_to_silver'

UPDATE metadata.config_table
SET source_folder = 'Products'
WHERE source_folder = 'Product'