import os
import sqlite3

# Create the data directory if it doesn't exist.
if not os.path.exists('data'):
    os.makedirs('data')

# Connect to the SQLite database.
db = sqlite3.connect('data/student_db.db')

# Create a cursor object.
cursor = db.cursor()

# Create a table called python_programming.
cursor.execute('''
CREATE TABLE IF NOT EXISTS python_programming (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER
)
''')
# Commit the creation of the table.
db.commit()

# Insert new rows into the python_programming table.
students = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]

cursor.executemany('''
INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)
''', students)
# Commit the insertion of new rows.
db.commit()

# Select all records with a grade between 60 and 80.
cursor.execute('''
SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80
''')
results = cursor.fetchall()
print("Records with grades between 60 and 80:")
for row in results:
    print(row)

# Change Carl Davis’s grade to 65.
cursor.execute('''
UPDATE python_programming SET grade = ? WHERE name = ?
''', (65, 'Carl Davis'))
# Commit the update.
db.commit()

# Delete Dennis Fredrickson’s row.
cursor.execute('''
DELETE FROM python_programming WHERE name = ?
''', ('Dennis Fredrickson',))
# Commit the deletion.
db.commit()

# Change the grade of all students with an id greater than 55 to a grade of 80.
cursor.execute('''
UPDATE python_programming SET grade = ? WHERE id > ?
''', (80, 55))
# Commit the update.
db.commit()

# Close the database connection.
db.close()
