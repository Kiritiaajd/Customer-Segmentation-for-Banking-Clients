import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",         # or your MySQL server address
    user="root",              # your MySQL username
    password="your_password", # your MySQL password
    database="purchasing_power_db" # the database you created
)

cursor = connection.cursor()

# Test the connection by running a query to fetch data
cursor.execute("SELECT * FROM customers LIMIT 5;")  # Fetch first 5 rows
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection when done
cursor.close()
connection.close()
