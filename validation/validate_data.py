import sqlite3
import pandas as pd

def validate_data():

    source_data = pd.read_csv(
        "data/processed_sales_data.csv"
    )

    conn = sqlite3.connect(
        "sales_data_warehouse.db"
    )

    db_data = pd.read_sql_query(
        "SELECT * FROM sales_analytics",
        conn
    )

    conn.close()

    print("Source Rows:", len(source_data))
    print("Database Rows:", len(db_data))

    if len(source_data) == len(db_data):
        print("Row Count Validation Passed")
    else:
        print("Row Count Validation Failed")

    print("\nMissing Values:")
    print(db_data.isnull().sum())

    print("\nDuplicate Rows:")
    print(db_data.duplicated().sum())

if __name__ == "__main__":
    validate_data()