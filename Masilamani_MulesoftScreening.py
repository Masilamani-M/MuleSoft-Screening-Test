import sqlite3
connection = sqlite3.connect('shows.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Mulesoft
              (MovieName TEXT,Actor TEXT,Actress TEXT, Year INT,Director TEXT)''')
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director) VALUES ('Vikram', 'Kamal Haasan', '-', 2022,'Lokesh Kanagaraj' )''')
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director)VALUES ('Master', 'Vijay', 'Malavika Mohan', 2021,'Lokesh Kanagaraj' )''')
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director)VALUES ('Don', 'Sivakarthikeyan', 'Priyanka Mohan', 2022,'Cibi Chakaravarthi' )''')
cursor.execute('''INSERT INTO Mulesoft (MovieName,Actor,Actress,Year,Director)VALUES ('Beast', 'Vijay', 'Pooja Hegde', 2022,'Nelson' )''')
cursor.execute('''SELECT * from Mulesoft''')
result = cursor.fetchall();
print(result)
connection.commit()
connection.close()
