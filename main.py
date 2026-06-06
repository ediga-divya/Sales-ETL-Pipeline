from extraction.extract_data import extract_data
from transformation.transform_data import transform_data
from loading.load_data import load_data

def main():

    print("=" * 50)
    print("SALES ETL PIPELINE STARTED")
    print("=" * 50)

    sales, customers, products = extract_data()

    final_data = transform_data(
        sales,
        customers,
        products
    )

    print("\nFinal Analytics Dataset:")
    print(final_data.head())

    output_path = load_data(final_data)

    print("\nRows Loaded:", len(final_data))
    print("Output File:", output_path)
    print("\nETL Pipeline Completed Successfully")

if __name__ == "__main__":
    main()