# MuleSoft-Screening-Test

#First we need to import the SQL in python
import sqlite3

#Create a connection between Python and SQL
connection = sqlite3.connect('shows.db')

#Create a Cursor Object
cursor = connection.cursor()

#Execution of Query
cursor.execute('''CREATE TABLE IF NOT EXISTS Mulesoft
              (MovieName TEXT,Actor TEXT,Actress TEXT, Year INT,Director TEXT)''')

#Execution of Query
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director) VALUES ('Vikram', 'Kamal Haasan', '-', 2022,'Lokesh Kanagaraj' )''')
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director)VALUES ('Master', 'Vijay', 'Malvika Mohan', 2021,'Lokesh Kanagaraj' )''')
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director)VALUES ('Master', 'Vijay Sethupathi', '', 2021,'Loki' )''')
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director)VALUES ('Red', 'AK', 'Sai', 2001,'Noper' )''')
cursor.execute('''SELECT * from Mulesoft''')

#Fetch the result
result = cursor.fetchall();

#Print the Result
print(result)
connection.commit()
#Close the connection
connection.close()
