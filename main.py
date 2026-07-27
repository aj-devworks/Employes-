# STEP 1A
# Import SQL Library and Pandas
import pandas as pd
import sqlite3

# STEP 1B
# Connect to the database
conn = sqlite3.connect("your_database.db")  # Replace with your .db file name


# STEP 2
# Retrieve first 5 rows
df_first_five = pd.read_sql_query("SELECT * FROM your_table LIMIT 5;", conn)

# STEP 3
# Retrieve 5 rows in reverse order (e.g., by ID)
df_five_reverse = pd.read_sql_query(
    "SELECT * FROM your_table ORDER BY id DESC LIMIT 5;", conn
)

# STEP 4
# Column aliasing
df_alias = pd.read_sql_query(
    "SELECT column_name AS alias_name FROM your_table;", conn
)

# STEP 5
# Filter records for Executive roles
df_executive = pd.read_sql_query(
    "SELECT * FROM your_table WHERE title LIKE '%Executive%';", conn
)

# STEP 6
# Get length of a name string
df_name_length = pd.read_sql_query(
    "SELECT name, LENGTH(name) AS name_length FROM your_table;", conn
)

# STEP 7
# Filter for titles shorter than a specific length
df_short_title = pd.read_sql_query(
    "SELECT * FROM your_table WHERE LENGTH(title) < 10;", conn
)

# STEP 8
# Sum total price aggregate
sum_total_price = pd.read_sql_query(
    "SELECT SUM(total_price) AS sum_total_price FROM your_table;", conn
)

# STEP 9
# Extract Day, Month, and Year from a date column
df_day_month_year = pd.read_sql_query(
    """
    SELECT 
        strftime('%d', date_column) AS Day,
        strftime('%m', date_column) AS Month,
        strftime('%Y', date_column) AS Year
    FROM your_table;
""",
    conn,
)