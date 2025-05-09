import psycopg2
from psycopg2.extras import execute_values
import pandas as pd


df = pd.DataFrame(data)

DB_HOST     = 'localhost'
DB_PORT     = 5432
DB_NAME     = 'your_database'
DB_USER     = 'your_user'
DB_PASSWORD = 'your_password'

table_name = 'mergent_companies'

connection = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = connection.cursor()

cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id SERIAL PRIMARY KEY,
    company_name TEXT,
    location TEXT,
    location_type TEXT,
    sales TEXT,
    sic TEXT,
    url TEXT,
    phone_number TEXT
)
""")
connection.commit()

rows = df[
    ['Company Name', 'Location', 'Location Type', 'Sales', 'SIC', 'URL', 'Phone Number']
].values.tolist()

insert_sql = f"""
INSERT INTO {table_name} (
    company_name, location, location_type, sales, sic, url, phone_number
) VALUES %s
ON CONFLICT DO NOTHING
"""
execute_values(cursor, insert_sql, rows)
connection.commit()

print(f"Inserted {cursor.rowcount} new records into {table_name}.")

cursor.close()
connection.close()
