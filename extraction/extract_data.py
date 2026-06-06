import pandas as pd

def extract_data():
    sales = pd.read_csv("data/sales.csv")
    customers = pd.read_csv("data/customers.csv")
    products = pd.read_csv("data/products.csv")

    print("Sales Data:")
    print(sales.head())

    print("\nCustomers Data:")
    print(customers.head())

    print("\nProducts Data:")
    print(products.head())

    return sales, customers, products

if __name__ == "__main__":
    extract_data()