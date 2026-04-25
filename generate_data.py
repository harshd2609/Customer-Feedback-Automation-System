import psycopg2
import random
from faker import Faker
from datetime import datetime

fake = Faker()

# PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    database="customer_database",
    user="postgres",
    password="8445"
)

cursor = conn.cursor()

departments = ["Sales", "HR", "IT", "Finance"]

# Fixed company list (better for dashboard analysis)
companies = [
    "Infosys",
    "Takkar_Polychem",
    "TCS",
    "Wipro",
    "Accenture",
    "HCL",
    "Deloitte",
    "Capgemini",
    "Cognizant"]

for _ in range(300):
    name = fake.name()
    email = fake.email()
    company = random.choice(companies)
    rating = random.randint(1, 5)
    feedback = fake.sentence(nb_words=8)
    department = random.choice(departments)
    current_date = fake.date_between(
        start_date="-6M",
        end_date="today"
    )

    query = """
    INSERT INTO customer_details
    (name, email, company, rating, feedback, department, date)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        name,
        email,
        company,
        rating,
        feedback,
        department,
        current_date
    )

    cursor.execute(query, values)

conn.commit()

print("300 Random Records Inserted Successfully!")
# Close connection
cursor.close()
conn.close()
