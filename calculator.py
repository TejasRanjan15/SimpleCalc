
import os
import psycopg2
from dotenv import load_dotenv

# Load secret settings from .env
load_dotenv()

# Connect to database
conn = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cursor = conn.cursor()

# Get input
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

# Calculate
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/" and b != 0:
    result = a / b
else:
    print("Invalid operation")
    cursor.close()
    conn.close()
    exit()

print("Result:", result)

# Save result
cursor.execute(
    "INSERT INTO calculations (num1, operator, num2, result) VALUES (%s, %s, %s, %s)",
    (a, op, b, result)
)

conn.commit()
print("Saved to database!")

cursor.close()
conn.close()
