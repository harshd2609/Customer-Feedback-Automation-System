# 🚀 Automated Customer Feedback ETL Pipeline

### Streamlit → PostgreSQL → Python ETL → Excel → Power BI

---

## 📌 Project Overview

This project is a complete **end-to-end automated ETL pipeline** designed for customer feedback management, reporting automation, and business intelligence.

It collects customer feedback using a **Streamlit form**, stores the data in **PostgreSQL**, processes and cleans the data using **Python ETL**, generates a reporting-ready **Excel dataset**, and finally visualizes insights using an interactive **Power BI Dashboard**.

The objective of this project is to reduce manual reporting efforts, improve data quality, automate repetitive tasks, and provide real-time business insights for better decision-making.

This project simulates a real-world workflow used in:

* Data Analytics
* Business Intelligence
* MIS Reporting
* Operations Management
* Dashboard Automation

---

# 🔄 Complete Workflow (Project Transitions)

```text id="flow01"
Customer/User Input
        ↓
Streamlit Form
        ↓
PostgreSQL Database Storage
        ↓
Python ETL Pipeline
        ↓
Data Cleaning & Transformation
        ↓
Cleaned Excel Dataset
        ↓
Power BI Dashboard
        ↓
Business Insights & Reporting
```

---

# ⚙️ Transition Breakdown

---

## 1️⃣ Streamlit Form → Data Collection

### Purpose

To create a user-friendly frontend where customers or users can submit feedback data.

### Input Fields

* Name
* Email
* Company
* Rating
* Feedback
* Department
* Date

### What Happens

User fills the form and clicks **Submit**

↓

Data is automatically pushed to PostgreSQL

---

## 2️⃣ PostgreSQL → Central Data Storage

### Purpose

To securely store all customer records in a structured database.

### Why PostgreSQL

* scalable
* reliable
* industry-standard
* better than manual Excel storage

### What Happens

Every new submission gets stored as a new row inside:

```sql id="tbl01"
customer_details
```

---

## 3️⃣ PostgreSQL → Python ETL Pipeline

### Purpose

To fetch raw data and prepare it for reporting.

### Python Handles

* Missing value treatment
* Duplicate removal
* Data formatting
* Standardization
* Validation
* Data quality checks

### What Happens

Raw SQL data becomes reporting-ready clean data

---

## 4️⃣ Python ETL → Excel Output

### Purpose

To create a final clean dataset for reporting and dashboard visualization.

### Output File

```text id="file01"
cleaned_customer_data.xlsx
```

### Why Excel

* easy Power BI connection
* stable reporting source
* easier business sharing

---

## 5️⃣ Excel → Power BI Dashboard

### Purpose

To transform clean data into business insights.

### Dashboard Includes

### KPI Cards

* Total Customers
* Average Rating
* Total Companies
* Positive Feedback Count

### Analytical Visuals

* Department-wise Rating Analysis
* Monthly Feedback Trend
* Company-wise Distribution
* Rating Distribution
* Customer Detail Table

### Interactive Filters

* Department Slicer
* Company Slicer
* Rating Filter
* Date Filter

---

## 6️⃣ Power BI → Decision Making

### Purpose

To help management take faster and better decisions.

### Business Value

* identifies low-performing departments
* tracks customer satisfaction
* analyzes feedback trends
* improves reporting speed
* reduces manual effort

---

# 🛠️ Technologies Used

## Backend

* Python
* Pandas
* Faker
* OpenPyXL
* Psycopg2

## Database

* PostgreSQL

## Frontend

* Streamlit

## Reporting & Visualization

* Microsoft Excel
* Microsoft Power BI


---

# 📁 Project Structure

```text id="struct01"
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
```

---

# 💼 Business Impact

This system automates the complete reporting pipeline and helps organizations reduce:

❌ Manual Excel reporting
❌ Human errors
❌ Time-consuming repetitive tasks

while improving:

✅ Data quality
✅ Reporting speed
✅ Dashboard accuracy
✅ Business decisions
✅ Operational efficiency

---

# 🎯 Why This Project is Strong

This is not just a college project.

It is a practical **industry-level ETL + Dashboard Automation Project** that solves a real business problem.

It demonstrates strong skills required for:

* Data Analyst Internship
* Business Analyst Internship
* MIS Executive Role
* Reporting Analyst Role
* Data Science Internship

---

# 👨‍💻 Author

## Harsh Diwakar

### MCA (Data Science)

Gautam Buddha University

📧 [harshdiwakar2609@gmail.com](mailto:harshdiwakar2609@gmail.com)

🔗 LinkedIn
[www.linkedin.com/in/harsh-diwakar-449928350](http://www.linkedin.com/in/harsh-diwakar-449928350)
