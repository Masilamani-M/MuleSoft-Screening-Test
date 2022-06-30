import sqlite3
connection = sqlite3.connect('shows.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Mulesoft
              (MovieName TEXT,Actor TEXT,Actress TEXT, Year INT,Director TEXT)''')
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director) VALUES ('Vikram', 'Kamal Haasan', '-', 2022,'Lokesh Kanagaraj' )''')
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director)VALUES ('Master', 'Vijay', 'Malvika Mohan', 2021,'Lokesh Kanagaraj' )''')
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director)VALUES ('Master', 'Vijay Sethupathi', '', 2021,'Loki' )''')
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director)VALUES ('Red', 'AK', 'Sai', 2001,'Noper' )''')
cursor.execute('''SELECT * from Mulesoft''')
result = cursor.fetchall();
print(result)
connection.commit()
connection.close()
