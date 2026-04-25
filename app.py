import streamlit as st
import psycopg2
from datetime import datetime
import subprocess

# PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    database="customer_database",
    user="postgres",
    password="8445"
)

cursor = conn.cursor()

# Streamlit Title
st.title("Customer Feedback Form")

# ----------------------------------
# Manual Customer Entry Form
# ----------------------------------

st.header("Manual Entry")

name = st.text_input("Enter Name")
email = st.text_input("Enter Email")
company = st.text_input("Enter Company")
rating = st.slider("Rating", 1, 5)
feedback = st.text_area("Feedback")
department = st.selectbox(
    "Department",
    ["Sales", "HR", "IT", "Finance"]
)

# Manual Submit Button
if st.button("Submit"):

    if name == "" or email == "" or company == "":
        st.warning("Please fill all required fields")

    else:
        current_date = datetime.now().date()

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

        try:
            # Insert into PostgreSQL
            cursor.execute(query, values)
            conn.commit()

            # Run ETL automatically
            subprocess.run(["python", "etl.py"])

            st.success("Data Submitted Successfully + Excel Updated!")

        except Exception as e:
            st.error(f"Error: {e}")

# ----------------------------------
# Random Data Generator Section
# ----------------------------------

st.header("Generate Random Data")

num_records = st.number_input(
    "Enter Number of Random Records",
    min_value=1,
    max_value=1000,
    value=300
)

# Random Data Button
if st.button("Generate Random Data"):

    try:
        # Run generate_data.py automatically
        subprocess.run(["python", "generate_data.py"])

        # Run ETL after random data generation
        subprocess.run(["python", "etl.py"])

        st.success(
            "Random Data Generated Successfully + Excel Updated!"
        )

    except Exception as e:
        st.error(f"Error: {e}")
