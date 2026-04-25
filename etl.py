import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'customer_database',
    user = 'postgres',
    password = '8445'
)

query = "SELECT * FROM customer_details"

df = pd.read_sql(query, conn)

print(df)

df.drop_duplicates(inplace = True)

df['rating'].fillna(df['rating'].median(),inplace = True)

df['name'] = df['name'].str.strip()

df.to_excel('Cleaned_Customer_Data.xlsx',index = False)

print('ETL Process Completed Successfully!')
