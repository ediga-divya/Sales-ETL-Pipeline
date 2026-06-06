import pandas as pd

def transform_data(sales, customers, products):

    sales["total_sales"] = (
        sales["quantity"] * sales["unit_price"]
    ) - sales["discount"]

    merged_data = sales.merge(
        customers,
        on="customer_id",
        how="left"
    )

    merged_data = merged_data.merge(
        products,
        on="product_id",
        how="left"
    )

    merged_data.drop_duplicates(inplace=True)

    merged_data.fillna("Unknown", inplace=True)

    return merged_data


if __name__ == "__main__":

    from extraction.extract_data import extract_data

    sales, customers, products = extract_data()

    transformed = transform_data(
        sales,
        customers,
        products
    )

    print(transformed.head())