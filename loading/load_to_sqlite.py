import sqlite3
import pandas as pd

def load_to_sqlite():

    data = pd.read_csv(
        "data/processed_sales_data.csv"
    )

    conn = sqlite3.connect(
        "sales_data_warehouse.db"
    )

    data.to_sql(
        "sales_analytics",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print(
        "Data loaded successfully into SQLite database."
    )

    print(
        "Database created: sales_data_warehouse.db"
    )

if __name__ == "__main__":
    load_to_sqlite()