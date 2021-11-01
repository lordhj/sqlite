import sqlite3
conn = sqlite3.connect("company.db")
cursorObj = conn.cursor()

""" Creating table employees
cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
"""

""" Inserting Data
cursorObj.execute("INSERT INTO employees VALUES(15, 'Emma', 20130, 'Helper', 'Head', '2002-01-08')")
conn.commit() # Saving all the changes"""

"""Updating
cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
conn.commit()"""

"""Selecting Data
cursorObj.execute('SELECT id, name FROM employees WHERE salary > 400.0') #Selecting Data
rows = cursorObj.fetchall() #Fetching the Selected Data
print(rows)
"""
conn.close()