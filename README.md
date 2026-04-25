🚀 Automated Customer Feedback ETL Pipeline
Using Streamlit • PostgreSQL • Python • Excel • Power BI
📌 Project Overview

This project is a complete end-to-end automated ETL pipeline built for customer feedback management, reporting automation, and business intelligence.

It collects customer feedback through a Streamlit form, stores data securely in PostgreSQL, performs automated ETL (Extract, Transform, Load) using Python, generates a cleaned Excel dataset, and visualizes insights through an interactive Power BI Dashboard.

The main goal of this project is to eliminate manual reporting, improve data quality, and provide real-time business insights using automation and dashboard analytics.

This project reflects a real-world workflow used in:

Data Analytics
Business Intelligence
MIS Reporting
Reporting Automation
Operations Management
🔄 Complete Project Flow
Streamlit Form
      ↓
PostgreSQL Database
      ↓
Python ETL Pipeline
      ↓
Cleaned Excel Dataset
      ↓
Power BI Dashboard
🛠 Tech Stack
Programming & Data
Python
Pandas
Faker
OpenPyXL
Psycopg2
Database
PostgreSQL
Frontend / Input System
Streamlit
Reporting & Visualization
Microsoft Excel
Microsoft Power BI
✨ Key Features
📥 Customer Data Collection
Interactive feedback form using Streamlit
Real-time user data entry
Direct database insertion
🗄 Database Integration
PostgreSQL-based structured storage
Secure and scalable data handling
Automatic record management
⚙ Automated ETL Pipeline

Python handles:

Missing value treatment
Duplicate removal
Data formatting
Standardization
Data validation
Clean dataset generation
🎲 Random Data Generator
Faker-based realistic dummy data generation
Bulk data insertion for dashboard analysis
Interview-ready dataset creation
📊 Interactive Power BI Dashboard

Dashboard includes:

KPI Cards
Total Customers
Average Rating
Total Companies
Positive Feedback Count
Analytical Visuals
Department-wise Rating Analysis
Monthly Feedback Trend
Company-wise Distribution
Rating Distribution Analysis
Customer Detail Table
Dynamic Filters
Department Slicer
Company Slicer
Rating Filter
Date Filter
📈 Dashboard Preview
Power BI Dashboard Screenshot

Add your dashboard screenshot here

![Dashboard Preview](dashboard_screenshot.png)

This makes your GitHub project much stronger for recruiters.

📁 Project Structure
Customer-Feedback-Automation/
│
├── app.py
├── etl.py
├── generate_data.py
├── cleaned_customer_data.xlsx
├── requirements.txt
├── README.md
├── dashboard_screenshot.png
└── .gitignore
⚡ Installation & Setup
Step 1 — Install Required Libraries
pip install -r requirements.txt
Step 2 — Create PostgreSQL Database
CREATE DATABASE customer_database;
Step 3 — Create Table
CREATE TABLE customer_details (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    company VARCHAR(100),
    rating INT,
    feedback TEXT,
    department VARCHAR(50),
    date DATE
);
Step 4 — Run Streamlit Application
streamlit run app.py
Step 5 — Run ETL Pipeline
python etl.py
Step 6 — Connect Excel to Power BI

Use:

cleaned_customer_data.xlsx

as the source file inside Power BI.

💼 Business Impact

This project significantly improves reporting workflows by automating:

Data collection
Data cleaning
Report generation
Dashboard visualization

It reduces:

❌ Manual Excel work
❌ Human errors
❌ Repetitive reporting tasks

and improves:

✅ Reporting speed
✅ Data quality
✅ Business decisions
✅ Operational efficiency

🎯 Why This Project Matters

This is not just a student project.

It is a practical industry-level automation system built around real business problems.

This project demonstrates strong skills required for:

Data Analyst Internship
Business Analyst Internship
MIS Executive Role
Reporting Analyst Role
Data Science Internship
🚀 Future Enhancements

Possible upgrades:

Email Report Automation
PDF Report Generation
Scheduled Power BI Auto Refresh
Direct PostgreSQL → Power BI Connection
Cloud Deployment using Streamlit Cloud
📄 Resume Project Description

Developed an end-to-end automated ETL pipeline using Streamlit, PostgreSQL, Python, Excel, and Power BI for customer feedback management. Automated data collection, preprocessing, transformation, and dashboard reporting to improve business insights and reduce manual reporting efforts.

👨‍💻 Author
Harsh Diwakar
MCA (Data Science)

📧 harshdiwakar2609@gmail.com

🔗 LinkedIn
www.linkedin.com/in/harsh-diwakar-449928350

⭐ Final Note

This project focuses on solving real business problems using:

Automation + Analytics + Visualization

instead of only theoretical machine learning models.

That is what makes it strong for internships, placements, and real-world industry roles.
