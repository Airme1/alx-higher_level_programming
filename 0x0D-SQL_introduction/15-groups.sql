-- list number of records with same score in second_table
SELECT score, COUNT(*) 
FROM second_table
WHERE score NOT UNIQUE
